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

def report_stats(analysis, filename='top95_test_stat_results.txt'):
    with open(filename, 'w') as file:
        for key, value in analysis.items():
            file.write(f"{key}:\n")
            file.write(f"  Average = {value['average']}\n")
            file.write(f"  Worst-case = {value['worst_case']}\n")
            file.write("\n")

def main():
    # Project Euler tests
    standard_stats = parse_stats('stat.txt')
    standard_analysis = analyze_stats(standard_stats)
    report_stats(standard_analysis, 'project_euler_test_stat_results.txt')

    # Top95 tests
    hard_stats = parse_stats('hard_stat.txt')
    hard_analysis = analyze_stats(hard_stats)
    report_stats(hard_analysis, 'top95_test_stat_results.txt')

if __name__ == '__main__':
    main()