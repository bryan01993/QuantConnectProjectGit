from typing import overload
from enum import Enum
import abc
import typing

import QuantConnect
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Algorithm.Framework.Portfolio.SignalExports
import QuantConnect.Interfaces
import System
import System.Collections.Generic


class SignalExportTargetParameters(System.Object):
    """Class to wrap objects needed to send signals to the different 3rd party API's"""

    @property
    def targets(self) -> System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Portfolio.PortfolioTarget]:
        """List of portfolio targets to be sent to some 3rd party API"""
        ...

    @property.setter
    def targets(self, value: System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Portfolio.PortfolioTarget]) -> None:
        ...

    @property
    def algorithm(self) -> QuantConnect.Interfaces.IAlgorithm:
        """Algorithm being ran"""
        ...

    @property.setter
    def algorithm(self, value: QuantConnect.Interfaces.IAlgorithm) -> None:
        ...


class BaseSignalExport(System.Object, QuantConnect.Interfaces.ISignalExportTarget, metaclass=abc.ABCMeta):
    """Base class to send signals to different 3rd party API's"""

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """
        The name of this signal export
        
        This property is protected.
        """
        ...

    @property
    def http_client(self) -> typing.Any:
        """
        Property to access a HttpClient
        
        This property is protected.
        """
        ...

    @property
    def allowed_security_types(self) -> System.Collections.Generic.HashSet[QuantConnect.SecurityType]:
        """
        Default hashset of allowed Security types
        
        This property is protected.
        """
        ...

    def dispose(self) -> None:
        """If created, dispose of HttpClient we used for the requests to the different 3rd party API's"""
        ...

    def send(self, parameters: QuantConnect.Algorithm.Framework.Portfolio.SignalExports.SignalExportTargetParameters) -> bool:
        """
        Sends positions to different 3rd party API's
        
        :param parameters: Holdings the user have defined to be sent to certain 3rd party API and the algorithm being ran
        :returns: True if the positions were sent correctly and the 3rd party API sent no errors. False, otherwise.
        """
        ...


class NumeraiSignalExport(QuantConnect.Algorithm.Framework.Portfolio.SignalExports.BaseSignalExport):
    """
    Exports signals of the desired positions to Numerai API.
    Accepts signals in percentage i.e numerai_ticker:"IBM US", signal:0.234
    """

    @property
    def name(self) -> str:
        """
        The name of this signal export
        
        This property is protected.
        """
        ...

    @property
    def allowed_security_types(self) -> System.Collections.Generic.HashSet[QuantConnect.SecurityType]:
        """
        Hashset property of Numerai allowed SecurityTypes
        
        This property is protected.
        """
        ...

    def __init__(self, publicId: str, secretId: str, modelId: str, fileName: str = "predictions.csv") -> None:
        """
        NumeraiSignalExport Constructor. It obtains the required information for Numerai API requests
        
        :param publicId: PUBLIC_ID provided by Numerai
        :param secretId: SECRET_ID provided by Numerai
        :param modelId: ID of the Numerai Model being used
        :param fileName: Signal file's name
        """
        ...

    def convert_targets_to_numerai(self, parameters: QuantConnect.Algorithm.Framework.Portfolio.SignalExports.SignalExportTargetParameters, positions: typing.Optional[str]) -> typing.Union[bool, str]:
        """
        Verifies each holding's signal is between 0 and 1 (exclusive)
        
        This method is protected.
        
        :param parameters: A list of portfolio holdings expected to be sent to Numerai API
        :param positions: A message with the desired positions in the expected Numerai API format
        :returns: True if a string message with the positions could be obtained, false otherwise.
        """
        ...

    def send(self, parameters: QuantConnect.Algorithm.Framework.Portfolio.SignalExports.SignalExportTargetParameters) -> bool:
        """
        Verifies all the given holdings are accepted by Numerai, creates a message with those holdings in the expected
        Numerai API format and sends them to Numerai API
        
        :param parameters: A list of portfolio holdings expected to be sent to Numerai API and the algorithm being ran
        :returns: True if the positions were sent to Numerai API correctly and no errors were returned, false otherwise.
        """
        ...


class CrunchDAOSignalExport(QuantConnect.Algorithm.Framework.Portfolio.SignalExports.BaseSignalExport):
    """
    Exports signals of the desired positions to CrunchDAO API.
    Accepts signals in percentage i.e ticker:"SPY", date: "2020-10-04", signal:0.54
    """

    @property
    def name(self) -> str:
        """
        The name of this signal export
        
        This property is protected.
        """
        ...

    @property
    def allowed_security_types(self) -> System.Collections.Generic.HashSet[QuantConnect.SecurityType]:
        """
        HashSet property of allowed SecurityTypes for CrunchDAO
        
        This property is protected.
        """
        ...

    def __init__(self, apiKey: str, model: str, submissionName: str = ..., comment: str = ...) -> None:
        """
        CrunchDAOSignalExport constructor. It obtains the required information for CrunchDAO API requests.
        See (https://colab.research.google.com/drive/1YW1xtHrIZ8ZHW69JvNANWowmxPcnkNu0?authuser=1#scrollTo=aPyWNxtuDc-X)
        
        :param apiKey: API key provided by CrunchDAO
        :param model: Model ID or Name
        :param submissionName: Submission Name (Optional)
        :param comment: Comment (Optional)
        """
        ...

    def convert_to_csv_format(self, parameters: QuantConnect.Algorithm.Framework.Portfolio.SignalExports.SignalExportTargetParameters, positions: typing.Optional[str]) -> typing.Union[bool, str]:
        """
        Converts the list of holdings into a CSV format string
        
        This method is protected.
        
        :param parameters: A list of holdings from the portfolio, expected to be sent to CrunchDAO API and the algorithm being ran
        :param positions: A CSV format string of the given holdings with the required features(ticker, date, signal)
        :returns: True if a string message with the positions could be obtained, false otherwise.
        """
        ...

    def send(self, parameters: QuantConnect.Algorithm.Framework.Portfolio.SignalExports.SignalExportTargetParameters) -> bool:
        """
        Verifies every holding is a stock, creates a message with the desired positions
        using the expected CrunchDAO API format, verifies there is an open round and then
        sends the positions with the other required body features. If another signal was
        submitted before, it deletes the last signal and sends the new one
        
        :param parameters: A list of holdings from the portfolio, expected to be sent to CrunchDAO API and the algorithm being ran
        :returns: True if the positions were sent to CrunchDAO succesfully and errors were returned, false otherwise.
        """
        ...


class SignalExportManager(System.Object):
    """
    Class manager to send portfolio targets to different 3rd party API's
    For example, it allows Collective2, CrunchDAO and Numerai signal export providers
    """

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        SignalExportManager Constructor, obtains the entry information needed to send signals
        and initializes the fields to be used
        
        :param algorithm: Algorithm being run
        """
        ...

    def add_signal_export_providers(self, *signal_exports: QuantConnect.Interfaces.ISignalExportTarget) -> None:
        """
        Adds one or more new signal exports providers
        
        :param signal_exports: One or more signal export provider
        """
        ...

    def get_portfolio_targets(self, targets: typing.Optional[typing.List[QuantConnect.Algorithm.Framework.Portfolio.PortfolioTarget]]) -> typing.Union[bool, typing.List[QuantConnect.Algorithm.Framework.Portfolio.PortfolioTarget]]:
        """
        Obtains an array of portfolio targets from algorithm's Portfolio and returns them.
        See  PortfolioTarget.Percent(IAlgorithm, Symbol, decimal, bool, string) for more
        information about how each symbol quantity was calculated
        
        This method is protected.
        
        :param targets: An array of portfolio targets from the algorithm's Portfolio
        :returns: True if TotalPortfolioValue was bigger than zero, false otherwise.
        """
        ...

    def set_target_portfolio(self, *portfolio_targets: QuantConnect.Algorithm.Framework.Portfolio.PortfolioTarget) -> bool:
        """
        Sets the portfolio targets with the given entries and sends them with the algorithm
        being ran to the signal exports providers set, as long as the algorithm is in live mode
        
        :param portfolio_targets: One or more portfolio targets to be sent to the defined signal export providers
        :returns: True if the portfolio targets could be sent to the different signal export providers successfully, false otherwise.
        """
        ...

    def set_target_portfolio_from_portfolio(self) -> bool:
        """
        Sets the portfolio targets from the algorihtm's Portfolio and sends them with the
        algorithm being ran to the signal exports providers already set
        
        :returns: True if the target list could be obtained from the algorithm's Portfolio and they were successfully sent to the signal export providers.
        """
        ...


class Collective2SignalExport(QuantConnect.Algorithm.Framework.Portfolio.SignalExports.BaseSignalExport):
    """
    Exports signals of desired positions to Collective2 API using JSON and HTTPS.
    Accepts signals in quantity(number of shares) i.e symbol:"SPY", quant:40
    """

    class Collective2Position(System.Object):
        """
        Stores position's needed information to be serialized in JSON format
        and then sent to Collective2 API
        
        This class is protected.
        """

        @property
        def c_2_symbol(self) -> QuantConnect.Algorithm.Framework.Portfolio.SignalExports.Collective2SignalExport.C2Symbol:
            """Position symbol"""
            ...

        @property.setter
        def c_2_symbol(self, value: QuantConnect.Algorithm.Framework.Portfolio.SignalExports.Collective2SignalExport.C2Symbol) -> None:
            ...

        @property
        def quantity(self) -> float:
            """
            Number of shares/contracts of the given symbol. Positive quantites are long positions
            and negative short positions.
            """
            ...

        @property.setter
        def quantity(self, value: float) -> None:
            ...

    class C2Symbol(System.Object):
        """
        The Collective2 symbol
        
        This class is protected.
        """

        @property
        def full_symbol(self) -> str:
            """The The full native C2 symbol e.g. BSRR2121Q22.5"""
            ...

        @property.setter
        def full_symbol(self, value: str) -> None:
            ...

        @property
        def symbol_type(self) -> str:
            """The type of instrument. e.g. 'stock', 'option', 'future', 'forex'"""
            ...

        @property.setter
        def symbol_type(self, value: str) -> None:
            ...

    @property
    def destination(self) -> System.Uri:
        """Collective2 API endpoint"""
        ...

    @property.setter
    def destination(self, value: System.Uri) -> None:
        ...

    @property
    def name(self) -> str:
        """
        The name of this signal export
        
        This property is protected.
        """
        ...

    def __init__(self, apiKey: str, systemId: int, useWhiteLabelApi: bool = False) -> None:
        """
        Collective2SignalExport constructor. It obtains the entry information for Collective2 API requests.
        See API documentation at https://trade.collective2.com/c2-api
        
        :param apiKey: API key provided by Collective2
        :param systemId: Trading system's ID number
        :param useWhiteLabelApi: Whether to use the white-label API instead of the general one
        """
        ...

    def convert_holdings_to_collective_2(self, parameters: QuantConnect.Algorithm.Framework.Portfolio.SignalExports.SignalExportTargetParameters, positions: typing.Optional[System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Portfolio.SignalExports.Collective2SignalExport.Collective2Position]]) -> typing.Union[bool, System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Portfolio.SignalExports.Collective2SignalExport.Collective2Position]]:
        """
        Converts a list of targets to a list of Collective2 positions
        
        This method is protected.
        
        :param parameters: A list of targets from the portfolio expected to be sent to Collective2 API and the algorithm being ran
        :param positions: A list of Collective2 positions
        :returns: True if the given targets could be converted to a Collective2Position list, false otherwise.
        """
        ...

    def convert_percentage_to_quantity(self, algorithm: QuantConnect.Interfaces.IAlgorithm, target: QuantConnect.Algorithm.Framework.Portfolio.PortfolioTarget) -> int:
        """
        Converts a given percentage of a position into the number of shares of it
        
        This method is protected.
        
        :param algorithm: Algorithm being ran
        :param target: Desired position to be sent to the Collective2 API
        :returns: Number of shares hold of the given position.
        """
        ...

    def create_message(self, positions: System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Portfolio.SignalExports.Collective2SignalExport.Collective2Position]) -> str:
        """
        Serializes the list of desired positions with the needed credentials in JSON format
        
        This method is protected.
        
        :param positions: List of Collective2 positions to be sent to Collective2 API
        :returns: A JSON request string of the desired positions to be sent by a POST request to Collective2 API.
        """
        ...

    def send(self, parameters: QuantConnect.Algorithm.Framework.Portfolio.SignalExports.SignalExportTargetParameters) -> bool:
        """
        Creates a JSON message with the desired positions using the expected
        Collective2 API format and then sends it
        
        :param parameters: A list of holdings from the portfolio expected to be sent to Collective2 API and the algorithm being ran
        :returns: True if the positions were sent correctly and Collective2 sent no errors, false otherwise.
        """
        ...


