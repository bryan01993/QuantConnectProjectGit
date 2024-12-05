# README.md

## Branches Overview

This project uses multiple branches to manage different stages of development, testing, and deployment of trading algorithms. Each branch is purpose-built for a specific type of workflow, ensuring the project remains organized and development progresses smoothly.

### Branches:

1. **develop** (Branch: `dev-branch`)
   - **Purpose**: The `develop` branch is intended for executing backtests and optimizations of trading algorithms. This environment is where initial work happens, allowing you to validate the logic, refine strategies, and optimize parameters before considering them for real-time use.
   - **Usage**: Use this branch for running historical data analysis, experimenting with new strategies, and optimizing configurations in a safe environment without any risk of executing real trades.

2. **paper** (Branch: `staging-branch`)
   - **Purpose**: The `paper` branch serves as the environment for placing algorithms in paper execution. This means simulating live trading with real-time market data without using actual funds. It is an essential step for testing the broker connections, evaluating the strategy's behavior in live conditions, and ensuring everything works as expected in real-time scenarios.
   - **Usage**: Use this branch to test the integration with broker APIs, evaluate the algorithm under simulated live market conditions, and fix any issues found before deploying to production.

3. **market** (Branch: `main-branch`)
   - **Purpose**: The `market` branch is dedicated to live execution using real market data and actual capital. It is the final stage where the validated and tested algorithms are deployed for live trading.
   - **Usage**: Only use this branch once you are confident in the reliability of the strategy. This branch is meant for fully validated algorithms that are ready to interact with real markets and execute actual trades.

## Project Architecture

For a detailed overview of the High-Level Design (HLD) and Low-Level Design (LLD) of the project, please refer to the following link:
[HLD and LLD Diagrams](https://lucid.app/lucidchart/c9edbce2-5053-44c4-82f5-1606b5491b89/edit?invitationId=inv_afe31877-2552-49e1-ae0e-ab3815e6cc23&page=lHWRpYG2GMFMI#)

## Summary
- The `develop` branch is used for backtesting and optimization.
- The `paper` branch is used for simulating live execution and testing connections.
- The `market` branch is used for real trading with live market data and actual funds.

Using these branches ensures a safe and structured workflow for developing, testing, and deploying trading algorithms while minimizing risks and maximizing reliability.

