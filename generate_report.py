import json
import os

def generate_html_report(json_file, output_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    def get_coverage_section(title, coverage_data):
        raw = coverage_data.get('raw', {})
        rate = coverage_data.get('rate', 'N/A')
        return f"""
        <tr>
            <td>{title}</td>
            <td>{raw.get('documented', 'N/A')}</td>
            <td>{raw.get('documentedAndTested', 'N/A')}</td>
            <td>{raw.get('totalTested', 'N/A')}</td>
            <td>{rate}</td>
        </tr>
        """

    html_content = f"""
    <html>
    <head>
        <title>Coverage Metrics Report</title>
        <style>
            table, th, td {{
                border: 1px solid black;
                border-collapse: collapse;
                padding: 8px;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Coverage Metrics Report</h1>
        <table>
            <tr>
                <th>Metric</th>
                <th>Documented</th>
                <th>Documented and Tested</th>
                <th>Total Tested</th>
                <th>Rate</th>
            </tr>
            {get_coverage_section('Path Coverage', data.get('pathCoverage', {}))}
            {get_coverage_section('Operation Coverage', data.get('operationCoverage', {}))}
            {get_coverage_section('Status Class Coverage', data.get('statusClassCoverage', {}))}
            {get_coverage_section('Status Coverage', data.get('statusCoverage', {}))}
            {get_coverage_section('Response Type Coverage', data.get('responseTypeCoverage', {}))}
            {get_coverage_section('Request Type Coverage', data.get('requestTypeCoverage', {}))}
            {get_coverage_section('Parameter Coverage', data.get('parameterCoverage', {}))}
            {get_coverage_section('Parameter Value Coverage', data.get('parameterValueCoverage', {}))}
        </table>
        <h3>TCL: {data.get('TCL', 'N/A')}</h3>
    </body>
    </html>
    """

    with open(output_file, 'w') as f:
        f.write(html_content)

    print(f"HTML report generated: {output_file}")

# Define the paths to the input JSON file and the output HTML file
json_file = './example/reports/stats.json'
output_file = './example/reports/coverage_report.html'

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

# Generate the HTML report
generate_html_report(json_file, output_file)