#region imports
from AlgorithmImports import *
#endregion

########################################################################################
#                                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");                      #
# you may not use this file except in compliance with the License.                     #
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0   #
#                                                                                      #
# Unless required by applicable law or agreed to in writing, software                  #
# distributed under the License is distributed on an "AS IS" BASIS,                    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.             #
# See the License for the specific language governing permissions and                  #
# limitations under the License.                                                       #
#                                                                                      #
# Copyright [2021] [Rocco Claudio Cannizzaro]                                          #
#                                                                                      #
########################################################################################

import numpy as np
from Logger import *
from BSMLibrary import *
from StrategyBuilder import *
from ContractUtils import *

class OptionStrategyOrderCore:

   # Internal counter for all the orders
   orderCount = 0

   # Default parameters
   defaultParameters = {
      "creditStrategy": True
      , "maxActivePositions": None
      , "maxOrderQuantity": 1
      , "slippage": 0.0
      , "profitTarget": 0.6
      , "stopLossMultiplier": 1.5
      # Minimum time distance between opening two consecutive trades
      , "minimumTradeScheduleDistance": timedelta(hours = 0)
      # If multiple expirations are available in the chain, should we use the furthest (True) or the earliest (False)
      , "useFurthestExpiry": True
      # Controls whether to consider the DTE of the last closed position when opening a new one:
      # If True, the Expiry date of the new position is selected such that the open DTE is the nearest to the DTE of the closed position
      , "dynamicDTESelection": False
      , "dte": 45
      , "dteWindow": 7
      , "dteThreshold": 21
      , "forceDteThreshold": False
      , "ditThreshold": None
      , "hardDitThreshold": None
      , "forceDitThreshold": False
      # Credit Targeting: either using a fixed credit amount (targetPremium) or a dynamic credit (percentage of Net Liquidity)
      , "targetPremiumPct": None
      , "targetPremium": None
      # Defines how the profit target is calculated. Valid options are (case insensitive):
      # - Premium: the profit target is a percentage of the premium paid/received. 
      # - Theta: the profit target is calculated based on the theta value of the position evaluated at self.thetaProfitDays from the time of entering the trade
      # - TReg: the profit target is calculated as a percentage of the TReg (MaxLoss + openPremium)
      # - Margin: the profit target is calculted as a percentage of the margin requirement (calculated based on self.portfolioMarginStress percentage upside/downside movement of the underlying)
      , "profitTargetMethod": "Premium"
      # Number of days into the future at which the theta of the position is calculated. Used if profitTargetMethod = "Theta"
      , "thetaProfitDays": None
      # Upside/Downside stress applied to the underlying to calculate the portfolio margin requirement of the position
      , "portfolioMarginStress": 0.12
      # Limit Order Management
      , "useLimitOrders": True
      , "limitOrderRelativePriceAdjustment": 0
      , "limitOrderAbsolutePrice": None
      , "limitOrderExpiration": timedelta(hours = 8)
      # Delta and Wing size used for Naked Put/Call and Spreads
      , "delta": 10
      , "wingSize": 10
      # Put/Call delta for Iron Condor
      , "putDelta": 10
      , "callDelta": 10
      # Net delta for Straddle, Iron Fly and Butterfly (using ATM strike if netDelta = None)
      , "netDelta": None
      # Put/Call Wing size for Iron Condor, Iron Fly
      , "putWingSize": 10
      , "callWingSize": 10
      # Butterfly specific parameters
      , "butteflyType": None
      , "butterflyLeftWingSize": 10
      , "butterflyRightWingSize": 10
      # If True, the order is submitted as long as it does not exceed the maxOrderQuantity.
      , "validateQuantity": True
      # If True, the order mid-price is validated to make sure the Bid-Ask spread is not too wide.
      , "validateBidAskSpread": False
      # Used when validateBidAskSpread = True. if the ratio between the bid-ask spread and the mid-price is higher than this parameter, the order is not executed
      , "bidAskSpreadRatio": 0.3
      # The time (on expiration day) at which any position that is still open will closed
      , "marketCloseCutoffTime": time(15, 45, 0)
      # Controls whether to include Cancelled orders (Limit orders that didn't fill) in the final output
      , "includeCancelledOrders": True
      # Controls whether to include details on each leg (open/close fill price and descriptive statistics about mid-price, Greeks, and IV)
      , "includeLegDetails": False
      # Controls which greeks are included in the output log
      , "greeksIncluded": ["Delta", "Gamma", "Vega", "Theta", "Rho", "Vomma", "Elasticity"]
      # Controls whether to track the details on each leg across the life of the trade
      , "trackLegDetails": False
      # Control whether to allow multiple positions to be opened for the same Expiration date
      , "allowMultipleEntriesPerExpiry": False
      # The frequency (in minutes) with which the leg details are updated (used only if includeLegDetails = True)
      , "legDatailsUpdateFrequency": 30
      # The frequency (in minutes) with which the position is managed
      , "managePositionFrequency": 1
      # Controls the memory (in minutes) of EMA process. The exponential decay is computed such that the contribution of each value decays by 95% after <emaMemory> minutes (i.e. decay^emaMemory = 0.05)
      , "emaMemory": 200
      # Ensures that the Stop Loss does not exceed the theoretical loss. (Set to False for Credit Calendars)
      , "capStopLoss": True
   }

   @staticmethod
   def getNextOrderId():
      OptionStrategyOrderCore.orderCount += 1
      return OptionStrategyOrderCore.orderCount


   # \param[in] context is a reference to the QCAlgorithm instance. The following attributes are used from the context:
   #    - slippage: (Optional) controls how the mid-price of an order is adjusted to include slippage.
   #    - targetPremium: (Optional) used to determine how many contracts to buy/sell.  
   #    - maxOrderQuantity: (Optional) Caps the number of contracts that are bought/sold (Default: 1). 
   #         If targetPremium == None  -> This is the number of contracts bought/sold.
   #         If targetPremium != None  -> The order is executed only if the number of contracts required to reach the target credit/debit does not exceed the maxOrderQuantity
   def __init__(self, context, name = None, nameTag = None, **kwargs):
      # Set the context (QCAlgorithm object)
      self.context = context
      # Set default name (use the class name) if no value has been provided 
      name = name or type(self).__name__
      # Set the Strategy Name
      self.name = name
      # Set the Strategy Name (optional)
      self.nameTag = nameTag or name
      # Set the logger
      self.logger = Logger(context, className = type(self).__name__, logLevel = context.logLevel)
      # Initialize the BSM pricing model
      self.bsm = BSM(context)
      # Initialize the contract utils
      self.contractUtils = ContractUtils(context)
      # Initialize the Strategy Builder
      self.strategyBuilder = StrategyBuilder(context)

      # Initialize the parameters dictionary with the default values
      self.parameters = OptionStrategyOrderCore.defaultParameters.copy()
      # Override default parameters with values that might have been set in the context
      for key in self.parameters:
         if hasattr(context, key):
            self.parameters[key] = getattr(context, key)
      # Now merge the dictionary with any kwargs parameters that might have been specified directly with the constructor (kwargs takes precedence)
      self.parameters.update(kwargs)

      # Determine what is the last trading day of the backtest
      self.endOfBacktestCutoffDttm = None
      if hasattr(context, "EndDate") and context.EndDate != None:
         self.endOfBacktestCutoffDttm = datetime.combine(self.lastTradingDay(context.EndDate), self.parameters["marketCloseCutoffTime"])
      
      # Create dictionary to keep track of all the open positions related to this strategy
      self.openPositions = {}
      # Create dictionary to keep track of all the working orders
      self.workingOrders = {}
      # Create dictionary to keep track of all the limit orders
      self.limitOrders = {}
      # Create FIFO list to keep track of all the recently closed positions (needed for the Dynamic DTE selection)
      self.recentlyClosedDTE = []
      
      # Keep track of the number of open positions that are specific to this strategy
      self.currentActivePositions = 0
      # Keep track of the number of working orders to open that are specific to this strategy
      self.currentWorkingOrdersToOpen = 0
      # Keep track of when was the last position opened 
      self.lastOpenedDttm = None


   # Interface method. Must be implemented by the inheriting class
   def setupCharts(self):
      pass
      
   # Interface method. Must be implemented by the inheriting class
   def updateCharts(self):
      pass
      
   # Interface method. Must be implemented by the inheriting class
   def getOrder(self, chain):
      pass
   
   def getMaxOrderQuantity(self):
      # Get the context
      context = self.context
      # Get the strategy parameters
      parameters = self.parameters
      
      # Get the maximum order quantity parameter
      maxOrderQuantity = parameters["maxOrderQuantity"]
      # Get the targetPremiumPct
      targetPremiumPct = parameters["targetPremiumPct"]
      # Check if we are using dynamic premium targeting
      if targetPremiumPct != None:
         # Scale the maxOrderQuantity consistently with the portfolio growth
         maxOrderQuantity = round(maxOrderQuantity * (1 + context.Portfolio.TotalProfit / context.initialAccountValue))
         # Make sure we don't go below the initial parameter value
         maxOrderQuantity = max(parameters["maxOrderQuantity"], maxOrderQuantity)
      # Return the result   
      return maxOrderQuantity


   def lastTradingDay(self, expiry):
      # Get the trading calendar
      tradingCalendar = self.context.TradingCalendar
      # Find the last trading day for the given expiration date
      lastDay = list(tradingCalendar.GetDaysByType(TradingDayType.BusinessDay, expiry - timedelta(days = 20), expiry))[-1].Date
      return lastDay

   def isDuplicateOrder(self, contracts, sides):
      # Loop through all working orders of this strategy
      for orderTag in list(self.workingOrders):
         # Get the current working order
         workingOrder = self.workingOrders.get(orderTag)
         # Check if the number of contracts of this working order is the same as the number of contracts in the input list
         if workingOrder and len(workingOrder) == len(contracts):
            # Initialize the isDuplicate flag. Assume it's duplicate unless we find a mismatch
            isDuplicate = True
            # Loop through each pair (contract, side)
            for contract, side in zip(contracts, sides):
               # Get the details of the contract
               contractInfo = workingOrder.get(contract.Symbol)
               # If we cannot find this contract then it's not a duplicate
               if contractInfo == None:
                  isDuplicate = False
                  break
               # Get the orderSide and expiryStr properties
               orderSide = contractInfo.get("orderSide")
               expiryStr = contractInfo.get("expiryStr")
               # Check for a mismatch
               if (orderSide != side # Found the contract but it's on a different side (Sell/Buy)
                   or expiryStr != contract.Expiry.strftime("%Y-%m-%d") # Found the contract but it's on a different Expiry
                   ):
                  # It's not a duplicate. Brake this innermost loop 
                  isDuplicate = False
                  break
            # Exit if we found a duplicate
            if isDuplicate:
               return isDuplicate

      # If we got this far, there are no duplicates
      return False
      
   # Create dictionary with the details of the order to be submitted
   def getOrderDetails(self, contracts, sides, strategy, sell = True, strategyId = None, expiry = None, sidesDesc = None):

      # Exit if there are no contracts to process
      if not contracts:
         return

      # Exit if we already have a working order for the same set of contracts and sides
      if self.isDuplicateOrder(contracts, sides):
         return
      
      # Get the context
      context = self.context
      # Get the strategy parameters
      parameters = self.parameters

      # Set the Strategy Id (if not specified)
      strategyId = strategyId or strategy.replace(" ", "")

      # Get the Expiration from the first contract (unless otherwise specified
      expiry = expiry or contracts[0].Expiry
      # Get the last trading day for the given expiration date (in case it falls on a holiday)
      expiryLastTradingDay = self.lastTradingDay(expiry)
      # Set the date/time threshold by which the position must be closed (on the last trading day before expiration)
      expiryMarketCloseCutoffDttm = datetime.combine(expiryLastTradingDay, parameters["marketCloseCutoffTime"])
      # Dictionary to map each contract symbol to the side (short/long) 
      contractSide = {}
      # Dictionary to map each contract symbol to its decription 
      contractSideDesc = {}
      # Dictionary to map each contract symbol to the actual contract object
      contractDictionary = {}
      
      # Dictionaries to keep track of all the strikes, Delta and IV
      strikes = {}
      delta = {}
      gamma = {}
      vega = {}
      theta = {}
      rho = {}
      vomma = {}
      elasticity = {}
      IV = {}
      midPrices = {}
      contractExpiry = {}

      # Compute the Greeks for each contract (if not already available)
      self.bsm.setGreeks(contracts)
      
      # Compute the Mid-Price and Bid-Ask spread for the full order
      orderMidPrice = 0.0
      bidAskSpread = 0.0
      # Get the slippage parameter (if available)
      slippage = parameters["slippage"] or 0.0
         
      # Get the limitOrderRelativePriceAdjustment
      limitOrderRelativePriceAdjustment = parameters["limitOrderRelativePriceAdjustment"] or 0.0
      # Get the limitOrderAbsolutePrice 
      limitOrderAbsolutePrice = parameters["limitOrderAbsolutePrice"]


      # Get the maximum order quantity
      maxOrderQuantity = self.getMaxOrderQuantity()
      # Get the targetPremiumPct
      targetPremiumPct = parameters["targetPremiumPct"]
      # Check if we are using dynamic premium targeting
      if targetPremiumPct != None:
         # Make sure targetPremiumPct is bounded to the range [0, 1])
         targetPremiumPct = max(0.0, min(1.0, targetPremiumPct))
         # Compute the target premium as a percentage of the total net portfolio value
         targetPremium = context.Portfolio.TotalPortfolioValue * targetPremiumPct
      else:
         targetPremium = parameters["targetPremium"]

      # Check if we have a description for the contracts
      if sidesDesc == None:
         # Temporary dictionaries to lookup a description
         optionTypeDesc = {OptionRight.Put: "Put", OptionRight.Call: "Call"}
         optionSideDesc = {-1: "short", 1: "long"}
         # create a description for each contract: <long|short><Call|Put>
         sidesDesc = list(map(lambda contract, side: f"{optionSideDesc[np.sign(side)]}{optionTypeDesc[contract.Right]}", contracts, sides))

      n = 0
      for contract in contracts:
         # Contract Side: +n -> Long, -n -> Short
         orderSide = sides[n]
         # Contract description (<long|short><Call|Put>)
         orderSideDesc = sidesDesc[n]
         
         # Store it in the dictionary
         contractSide[contract.Symbol] = orderSide
         contractSideDesc[contract.Symbol] = orderSideDesc
         contractDictionary[contract.Symbol] = contract

         # Set the strike in the dictionary -> "<short|long><Call|Put>": <strike>
         strikes[f"{orderSideDesc}"] = contract.Strike
         contractExpiry[f"{orderSideDesc}"] = contract.Expiry
         # Set the Greeks and IV in the dictionary -> "<short|long><Call|Put>": <greek|IV>
         delta[f"{orderSideDesc}"] = contract.BSMGreeks.Delta
         gamma[f"{orderSideDesc}"] = contract.BSMGreeks.Gamma
         vega[f"{orderSideDesc}"] = contract.BSMGreeks.Vega
         theta[f"{orderSideDesc}"] = contract.BSMGreeks.Theta
         rho[f"{orderSideDesc}"] = contract.BSMGreeks.Rho
         vomma[f"{orderSideDesc}"] = contract.BSMGreeks.Vomma
         elasticity[f"{orderSideDesc}"] = contract.BSMGreeks.Elasticity
         IV[f"{orderSideDesc}"] = contract.BSMImpliedVolatility

         # Get the latest mid-price
         midPrice = self.contractUtils.midPrice(contract)
         # Store the midPrice in the dictionary -> "<short|long><Call|Put>": midPrice
         midPrices[f"{orderSideDesc}"] = midPrice
         # Compute the bid-ask spread
         bidAskSpread += self.contractUtils.bidAskSpread(contract)         
         # Adjusted mid-price (include slippage). Take the sign of orderSide to determine the direction of the adjustment
         adjustedMidPrice = midPrice + np.sign(orderSide) * slippage
         # Keep track of the total credit/debit or the order
         orderMidPrice -= orderSide * midPrice

         # Increment counter
         n += 1
      
      # Compute Limit Order price
      if limitOrderAbsolutePrice != None:
         if abs(orderMidPrice) < 1e-5:
            limitOrderRelativePriceAdjustment = 0
         else:
            # Compute the relative price adjustment (needed to adjust each leg with the same proportion)
            limitOrderRelativePriceAdjustment = limitOrderAbsolutePrice / orderMidPrice - 1
         # Use the specified absolute price
         limitOrderPrice = limitOrderAbsolutePrice
      else:
         # Set the Limit Order price (including slippage)
         limitOrderPrice = orderMidPrice * (1 + limitOrderRelativePriceAdjustment)

      # Compute the total slippage
      totalSlippage = sum(list(map(abs, sides))) * slippage
      # Add slippage to the limit order
      limitOrderPrice -= totalSlippage

      # Round the prices to the nearest cent
      orderMidPrice = round(orderMidPrice, 2)
      limitOrderPrice = round(limitOrderPrice, 2)

      # Determine which price is used to compute the order quantity
      if parameters["useLimitOrders"]:
         # Use the Limit Order price
         qtyMidPrice = limitOrderPrice
      else:
         # Use the contract mid-price
         qtyMidPrice = orderMidPrice      

      if targetPremium == None:
         # No target premium was provided. Use maxOrderQuantity
         orderQuantity = maxOrderQuantity
      else:   
         # Make sure we are not exceeding the available portfolio margin
         targetPremium = min(context.Portfolio.MarginRemaining, targetPremium)

         # Determine the order quantity based on the target premium
         if abs(qtyMidPrice) <= 1e-5:
            orderQuantity = 1
         else:
            orderQuantity = abs(targetPremium / (qtyMidPrice * 100))
         
         # Different logic for Credit vs Debit strategies
         if sell: # Credit order
            # Sell at least one contract
            orderQuantity = max(1, round(orderQuantity))
         else: # Debit order
            # Make sure the total price does not exceed the target premium
            orderQuantity = math.floor(orderQuantity)


      # Internal function to evaluate the P&L of the position
      def fValue(spotPrice, contracts, sides = None, atTime = None, openPremium = None):
         # Compute the theoretical value at the given Spot price and point in time
         prices = np.array([self.bsm.bsmPrice(contract
                                              , sigma = contract.BSMImpliedVolatility
                                              , spotPrice = spotPrice
                                              , atTime = atTime
                                              )
                              for contract in contracts
                            ]
                           )
         # Total value of the position
         value = openPremium + sum(prices * np.array(sides))
         return value

      # Get the current price of the underlying
      security = context.Securities[context.underlyingSymbol]
      underlyingPrice = context.GetLastKnownPrice(security).Price

      # Compute MaxLoss
      maxLoss = self.computeOrderMaxLoss(contracts, sides)
      # Get the Profit Target percentage is specified (default is 50%)
      profitTargetPct = parameters.get("profitTarget", 0.5)
      #Compute T-Reg margin based on the MaxLoss
      TReg = min(0, orderMidPrice + maxLoss) * orderQuantity

      portfolioMarginStress = parameters.get("portfolioMarginStress")
      # Compute the projected P&L of the position following a % movement of the underlying up or down
      portfolioMargin = min(0
                            , fValue(underlyingPrice * (1-portfolioMarginStress), contracts, sides = sides, atTime = context.Time, openPremium = midPrice)
                            , fValue(underlyingPrice * (1+portfolioMarginStress), contracts, sides = sides, atTime = context.Time, openPremium = midPrice)
                            ) * orderQuantity


      # Create order details
      order = {"expiry": expiry
               , "expiryStr": expiry.strftime("%Y-%m-%d")
               , "expiryLastTradingDay": expiryLastTradingDay
               , "expiryMarketCloseCutoffDttm": expiryMarketCloseCutoffDttm
               , "strategyId": strategyId
               , "strategy": strategy
               , "sides": sides
               , "sidesDesc": sidesDesc
               , "contractExpiry": contractExpiry
               , "contractSide": contractSide
               , "contractSideDesc": contractSideDesc
               , "contractDictionary": contractDictionary
               , "strikes": strikes
               , "midPrices": midPrices
               , "delta": delta
               , "gamma": gamma
               , "vega": vega
               , "theta": theta
               , "rho": rho
               , "vomma": vomma
               , "elasticity": elasticity
               , "IV": IV
               , "contracts": contracts
               , "targetPremium": targetPremium
               , "maxOrderQuantity": maxOrderQuantity
               , "orderQuantity": orderQuantity
               , "creditStrategy": sell
               , "maxLoss": maxLoss
               , "TReg": TReg
               , "portfolioMargin": portfolioMargin
               , "open": {"orders": []
                          , "fills": 0
                          , "filled": False
                          , "stalePrice": False
                          , "limitOrderAdjustment": limitOrderRelativePriceAdjustment
                          , "orderMidPrice": orderMidPrice
                          , "limitOrderPrice": limitOrderPrice
                          , "qtyMidPrice": qtyMidPrice
                          , "limitOrder": parameters["useLimitOrders"]
                          , "limitOrderExpiryDttm": context.Time + parameters["limitOrderExpiration"]
                          , "slippage": slippage
                          , "totalSlippage": totalSlippage
                          , "bidAskSpread": bidAskSpread
                          , "fillPrice": 0.0
                          }
               , "close": {"orders": []
                           , "fills": 0
                           , "filled": False
                           , "stalePrice": False
                           , "orderMidPrice": 0.0
                           , "fillPrice": 0.0
                           }
            }


      # Determine the method used to calculate the profit target
      profitTargetMethod = (parameters.get("profitTargetMethod", "Premium") or "Premium").lower()
      thetaProfitDays = parameters.get("thetaProfitDays", 0) or 0
      # Set a custom profit target unless we are using the default Premium based methodology
      if profitTargetMethod != "premium":
         if profitTargetMethod == "theta" and thetaProfitDays > 0:
            # Calculate the P&L of the position at T+[thetaProfitDays]
            thetaPnL = fValue(underlyingPrice, contracts, sides = sides, atTime = context.Time + timedelta(days = thetaProfitDays), openPremium = midPrice)
            # Profit target is a percentage of the P&L calculated at T+[thetaProfitDays]
            profitTargetAmt = profitTargetPct * abs(thetaPnL) * orderQuantity
         elif profitTargetMethod == "treg":
            # Profit target is a percentage of the TReg requirement
            profitTargetAmt = profitTargetPct * abs(TReg) * orderQuantity
         elif profitTargetMethod == "margin":
            # Profit target is a percentage of the margin requirement
            profitTargetAmt = profitTargetPct * abs(portfolioMargin) * orderQuantity
         else:
            pass
         # Set the target profit for the position
         order["targetProfit"] = profitTargetAmt

      return order


   def getPayoff(self, spotPrice, contracts, sides):
      # Exit if there are no contracts to process
      if len(contracts) == 0:
         return 0

      # Initialize the counter
      n = 0
      # initialize the payoff
      payoff = 0
      for contract in contracts:
         # direction: Call -> +1, Put -> -1
         direction = 2*int(contract.Right == OptionRight.Call)-1
         # Add the payoff of the current contract
         payoff += sides[n] * max(0, direction * (spotPrice - contract.Strike))
         # Increment the counter
         n += 1

      # Return the payoff
      return payoff
      
   def computeOrderMaxLoss(self, contracts, sides):
      # Exit if there are no contracts to process
      if len(contracts) == 0:
         return 0

      # Get the current price of the underlying
      UnderlyingLastPrice = self.contractUtils.getUnderlyingLastPrice(contracts[0])
      # Evaluate the payoff at the extreme (spotPrice = 0)
      maxLoss = self.getPayoff(0, contracts, sides)
      # Evaluate the payoff at each strike
      for contract in contracts:
         maxLoss = min(maxLoss, self.getPayoff(contract.Strike, contracts, sides))

      # Evaluate the payoff at the extreme (spotPrice = 10x higher)
      maxLoss = min(maxLoss, self.getPayoff(UnderlyingLastPrice*10, contracts, sides))      
      # Cap the payoff at zero: we are only interested in losses
      maxLoss = min(0, maxLoss)
      # Return the max loss
      return maxLoss

   def getCustomOrder(self, contracts, types, deltas = None, sides = None, sidesDesc = None, strategy = "Custom", sell = None):

      # Make sure the Sides parameter has been specified
      if not sides:
         self.logger.error("Input parameter sides cannot be null. No order will be returned.")
         return
      
      # Make sure the Sides and Deltas parameters are of the same length
      if not deltas or len(deltas) != len(sides):
         self.logger.error(f"Input parameters deltas = {deltas} and sides = {sides} must have the same length. No order will be returned.")
         return
      
      # Convert types into a list if it is a string
      if isinstance(types, str):
         types = [types] * len(sides)

      # Make sure the Sides and Types parameters are of the same length
      if not types or len(types) != len(sides):
         self.logger.error(f"Input parameters types = {types} and sides = {sides} must have the same length. No order will be returned.")
         return

      legs = []
      midPrice = 0
      for side, type, delta in zip(sides, types, deltas):
         # Get all Puts with a strike lower than the given putStrike and delta lower than the given putDelta
         deltaContracts = self.strategyBuilder.getContracts(contracts, type = type, toDelta = delta, reverse = type.lower() == "put")
         # Exit if we could not find the contract
         if not deltaContracts:
            return
         # Append the contract to the list of legs
         legs = legs + [deltaContracts[0]]
         # Update the mid-price
         midPrice -= self.contractUtils.midPrice(deltaContracts[0]) * side
      
      # Automatically determine if this is a credit or debit strategy (unless specified)
      if sell is None:
         sell = midPrice > 0
         
      # Create order details
      order = self.getOrderDetails(legs, sides, strategy, sell = sell, sidesDesc = sidesDesc)
      # Return the order
      return order

