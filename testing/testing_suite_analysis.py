#!/usr/bin/env python3

def parse_stats(file_path):
    stats = {
        'restarts': [],
        'conflicts': [],
        'decisions': [],
        'propagations': [],
        'conflict_literals': [],
        'memory_used': [],
        'cpu_time': []
    }
    current_test = {}

    with open(file_path, 'r') as file:
        for line in file:
            if 'restarts' in line:
                current_test['restarts'] = int(line.split(':')[1].strip())
            elif 'conflicts' in line:
                current_test['conflicts'] = int(line.split(':')[1].split()[0].strip())
            elif 'decisions' in line:
                current_test['decisions'] = int(line.split(':')[1].split()[0].strip())
            elif 'propagations' in line:
                current_test['propagations'] = int(line.split(':')[1].split()[0].strip())
            elif 'conflict literals' in line:
                try:
                    current_test['conflict_literals'] = int(line.split(':')[1].split()[0].strip())
                except ValueError:
                    current_test['conflict_literals'] = 0
            elif 'Memory used' in line:
                current_test['memory_used'] = float(line.split(':')[1].split()[0].strip())
            elif 'CPU time' in line:
                current_test['cpu_time'] = float(line.split(':')[1].split()[0].strip())

                for key in stats:
                    stats[key].append(current_test.get(key, 0))

                current_test = {}

    return stats

def analyze_stats(stats):
    analysis = {}

    for key in stats:
        values = stats[key]
        analysis[key] = {
            'average': sum(values) / len(values) if values else 0,
            'worst_case': max(values) if values else 0
        }

    return analysis

def report_stats(analysis, filename):
    with open(filename, 'w') as file:
        file.write(f"Analysis for {filename}:\n")
        for key, value in analysis.items():
            file.write(f"{key}:\n")
            file.write(f"  Average = {value['average']}\n")
            file.write(f"  Worst-case = {value['worst_case']}\n")
            file.write("\n")

def main():
    versions = [1, 2, 3]
    test_types = [('project_euler', 'stat_v'), ('top95', 'hard_stat_v')]

    for version in versions:
        for test_name, file_prefix in test_types:
            file_path = f'{file_prefix}{version}.txt'
            stats = parse_stats(file_path)
            analysis = analyze_stats(stats)
            report_filename = f'{test_name}_test_stat_results_v{version}.txt'
            report_stats(analysis, report_filename)

if __name__ == '__main__':
    main()