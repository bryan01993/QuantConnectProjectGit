import re
import pandas as pd
import plotly.express as px
def read_log_file(file_path):
    log_data = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r"Calling function: (\d+-[\w-]+) \| Execution time: ([\d.]+)s \| Args: (.+)", line)
            if match:
                function_name, exec_time, args = match.groups()
                log_data.append({
                    'function_name': function_name,
                    'execution_time': float(exec_time),
                    'args': args
                })
    return log_data

# Example usage:
log_file_path = 'path_to_log_file.txt'
log_data = read_log_file(log_file_path)

def create_dataframe(log_data):
    df = pd.DataFrame(log_data)
    return df

# Example usage:
df = create_dataframe(log_data)


def calculate_average_execution_time(df):
    avg_exec_time = df.groupby('function_name')['execution_time'].mean().reset_index()
    avg_exec_time.rename(columns={'execution_time': 'avg_execution_time'}, inplace=True)
    return avg_exec_time

# Example usage:
avg_exec_time_df = calculate_average_execution_time(df)



def create_gantt_chart(avg_exec_time_df):
    fig = px.bar(avg_exec_time_df,
                 x='avg_execution_time',
                 y='function_name',
                 orientation='h',
                 title='Average Execution Time of Functions',
                 labels={'avg_execution_time': 'Average Execution Time (s)', 'function_name': 'Function Name'})
    fig.show()

# Example usage:
create_gantt_chart(avg_exec_time_df)