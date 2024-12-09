import os
import pysqlite3


class QuantConnectDBHandler:
    def __init__(self, db_name='quantconnect_results.db'):
        """Initialize the database handler with a connection to the SQLite database."""
        # Define the database path within the root/Database folder
        database_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Database', db_name)
        self.db_name = database_path
        self.conn = pysqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """Create the BTOPResults, BTOPOrders, and AlgoMetrics tables if they do not exist."""
        # Create BTOPResults table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS BTOPResults (
            id TEXT PRIMARY KEY,
            strategy_name TEXT,
            backtest_date TEXT,
            cumulative_return REAL,
            sharpe_ratio REAL
        )
        """)

        # Create BTOPOrders table
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS BTOPOrders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            btop_result_id TEXT,
            order_id TEXT,
            strategy_name TEXT,
            order_type TEXT,
            quantity INTEGER,
            price REAL,
            timestamp TEXT,
            FOREIGN KEY (btop_result_id) REFERENCES BTOPResults (id)
        )
        """)

        # Create AlgoMetrics table (schema left undefined for now)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS AlgoMetrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT
            -- Additional columns to be defined later
        )
        """)

        self.conn.commit()

    def write_results(self, results):
        """Insert multiple rows of backtest results into the BTOPResults table.

        Args:
            results (list of tuple): List of tuples containing id, strategy_name, backtest_date,
                                    cumulative_return, and sharpe_ratio.
        """
        self.cursor.executemany("""
        INSERT INTO BTOPResults (id, strategy_name, backtest_date, cumulative_return, sharpe_ratio)
        VALUES (?, ?, ?, ?, ?)
        """, results)
        self.conn.commit()

    def write_orders(self, orders):
        """Insert multiple rows of order data into the BTOPOrders table.

        Args:
            orders (list of tuple): List of tuples containing btop_result_id, order_id, strategy_name,
                                    order_type, quantity, price, and timestamp.
        """
        self.cursor.executemany("""
        INSERT INTO BTOPOrders (btop_result_id, order_id, strategy_name, order_type, quantity, price, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, orders)
        self.conn.commit()

    def read_results(self):
        """Read all results from the BTOPResults table.

        Returns:
            list of tuple: All rows from the table.
        """
        self.cursor.execute("SELECT * FROM BTOPResults")
        return self.cursor.fetchall()

    def read_orders(self):
        """Read all orders from the BTOPOrders table.

        Returns:
            list of tuple: All rows from the table.
        """
        self.cursor.execute("SELECT * FROM BTOPOrders")
        return self.cursor.fetchall()

    def close(self):
        """Close the database connection."""
        self.conn.close()


# Make the class callable from other scripts
if __name__ == "__main__":
    print("This module is meant to be imported and used by other scripts.")
