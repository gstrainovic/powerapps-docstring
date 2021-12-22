import os, sys, getopt
import yaml
from powerapps_docstring.powerapp import PowerApp, UnknownSourceException, CanvasManifestNotFoundInSourceException
from powerapps_docstring.documentation import Docstring
import gh_md_to_html


def main(argv):
    pa_src_path = "example/src/meetingcapturedemo"
    output_path = "example"
    config_file = "config.yaml"

    if not os.path.isfile(config_file):
        print(f"The config file: {config_file} is not valid.")
        print("Refere to the help with -h or --help")
        sys.exit(1)
    else:
        with open(config_file, "r", encoding='utf8') as file:
            config = yaml.safe_load(file)

    # run documentation creation process
    print(f"Creating documentation for {pa_src_path}")
    try:
        docstring = Docstring(pa_src_path, output_path, config)
        documentation_output_path = docstring.create_documentation()
        print(f"Markdown Documentation created successfully: {documentation_output_path}")

        print(f"Start HTML Documentation creating")
        html_path = documentation_output_path + '.html'
        html = gh_md_to_html.main(documentation_output_path)
        
        with open(html_path, "w") as html_file:
            html_file.write(html)
        html_file.close

        with open(html_path) as fin:
            html_lines = fin.readlines()
        fin.close

        new_lines = [r'<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>']
        new_lines.append(r'<script>mermaid.initialize({ startOnLoad: true });</script>')

        for line in html_lines:
            if ':::' or '<br/>' in line:
                line = (line.replace('<br/>', ''))
                line = (line.replace(':::mermaid', '<div class="mermaid">'))
                line = (line.replace(':::', '</div>'))
                new_lines.append(line)
            else:
                new_lines.append(line)

        fout = open(documentation_output_path + '.html', "w")
        fout.writelines(new_lines)
        fout.close()
        print(f"HTML Documentation created successfully: {html_path}")

        sys.exit(0)
    except Exception as e:
        print("Error occured within documentation creation")
        raise e

def print_help():
    print(main.__doc__)

if __name__ == "__main__":
    main(sys.argv[1:])