import glob
import sys
import yaml
import csv

def main(argv):
    pa_src_path = "example/src/*/Src/*.yaml"
    filenames = glob.glob(pa_src_path)

    def get_screen_content(screen_name):
        screen_path = screen_name 
        screen_content = {}

        with open(screen_path, "r", encoding='utf8') as file:
            screen_content = yaml.load(file, Loader=yaml.BaseLoader)

        return screen_content


    def find_keys(d, target):
        for k, v in d.items():
            if target in k:
                return [k]
            if isinstance(v, dict):
                p = find_keys(v, target)
                if p:
                    return [k] + p



    def find_value_from_key(d, target):
        for k, v in d.items():
            if target in k:
                yield v
            if isinstance(v, dict):
                for i in find_value_from_key(v, target):
                    yield i

    output_csv = open('output.csv', 'w', newline='')
    csv_writer = csv.writer(output_csv, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['as', 'key', 'value', 'status'])


    # opening the file using "with"
    # statement
    with open('input.csv') as input_csv:
        for line in csv.DictReader(input_csv):
            asScreen = line['as']
            key = line['key']
            value = line['value']

            for file in filenames:
                print(file)
                screen_content = get_screen_content(file)

                arr = []
                for val in find_value_from_key(screen_content, asScreen):
                    arr.append(val)

                if arr: # asScreen found
                    keys = find_keys(screen_content, key)
                    if keys and not value:
                        nvalue = arr[0][key]
                        mytuple = asScreen, key, nvalue, 'value read ok'
                        print(mytuple)
                        csv_writer.writerow(mytuple)
                    if keys and value:
                        arr[0][key] = "=helloWorld"
                        #kk = ['CameraScreen As screen']['CameraNavBar As group']['AppLogo3 As image']['ImagePosition']
                        
                        # don't work
                        ## screen_content.update(arr[0][key])
                        
                        # with open(r'new.yaml', 'w') as write_yaml:
                        #     documents = yaml.dump(screen_content, write_yaml)
                        mytuple = asScreen, key, value, 'value replace ok'
                        print(mytuple)
                        csv_writer.writerow(mytuple)
                    if not keys and value:
                        mytuple = asScreen, key, value, 'add key and value ok'
                        print(mytuple)
                        csv_writer.writerow(mytuple)


    return ''
def print_help():
    print(main.__doc__)

if __name__ == "__main__":
    main(sys.argv[1:])