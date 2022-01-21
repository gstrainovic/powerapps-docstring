import glob
import sys
import csv


def main(argv):
    pa_src_path = "example/src/*/Src/*.yaml"
    filenames = glob.glob(pa_src_path)

    def finder(screen_content, asScreen, key):
        key = key + ':'
        asFound = False
        ar = []
        for line in screen_content:
            if asScreen in line:
                asFound = True
            elif asFound:
                if key in line:
                    start_index = line.find(key)
                    old_value = line[start_index + len(key):]
                    if start_index != -1:
                        return old_value.strip(), 'screen,key,value found'
                elif line == '\n':
                    asFound = False
                    return '', 'screen found, key not found'

    def replaceOrAdd(screen_content, asScreen, key, new_value, status):
        key = key + ':'
        asFound = False
        ar = []
        for line in screen_content:
            if asScreen in line and 'As' in line:
                spaces_start_count = len(line) - len(line.lstrip()) + 4
                spaces_start = spaces_start_count * ' '
                asFound = True
            elif asFound:
                if key in line and status=='replace':  # replace
                    start_index = line.find(key)
                    old_value = line[start_index + len(key):].strip()
                    line = line.replace(old_value, new_value)
                    status='replaced'
                elif line == '\n' and status=='add':  # add line
                    ar.append(spaces_start +
                              key + " " + new_value)
                    ar.append('\n')
                    asFound = False

            ar.append(line)

        return ar

    output_csv = open('output.csv', 'a', newline='')
    csv_writer = csv.writer(output_csv, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # csv_writer.writerow(['as', 'key', 'value', 'status'])

    with open('input.csv', 'r') as input_csv:
        for line in csv.DictReader(input_csv):
            asScreen = line['as']
            key = line['key']
            value_from_csv = line['value']

            for filepath in filenames:
                with open(filepath, encoding='utf8') as file:
                    screen_content = file.readlines()

                find_result = finder(screen_content, asScreen, key)

                if find_result:
                    value_in_yaml, status = find_result

                    # find value
                    if not value_from_csv and status == 'screen,key,value found':
                        mytuple = asScreen, key, value_in_yaml, 'value read ok'


                    # replace
                    elif value_from_csv and status == 'screen,key,value found':
                        new_yaml = replaceOrAdd(
                            screen_content, asScreen, key, value_from_csv, 'replace')

                        with open(filepath, 'w') as write_yaml:
                            write_yaml.writelines(new_yaml)

                        mytuple = asScreen, key, value_from_csv, 'value replace ok'

                    # add new line
                    elif value_from_csv and status == 'screen found, key not found':
                        new_yaml = replaceOrAdd(
                            screen_content, asScreen, key, value_from_csv, 'add')

                        with open(filepath, 'w') as write_yaml:
                            write_yaml.writelines(new_yaml)

                        mytuple = asScreen, key, value_from_csv, 'add key and value ok'

                    print(filepath)
                    print(mytuple)
                    csv_writer.writerow(mytuple)

    return ''


def print_help():
    print(main.__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
