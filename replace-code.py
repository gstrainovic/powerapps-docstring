import sys
import glob
import re
from shutil import copyfile

"""
    Replace all values with UpdateIf([Table],Lookup(...),{xxx}) with Patch([Table],ThisItem,{xxx}).
    The column of the lookup can contain different values. The table name [Table] and {xxx} should remain identical.   
    The lookup is omitted and replaced by ThisItem.

    Example:

        From:
        UpdateIf(colQuestionRow,ID218=ThisItem.ID218,{Edit: "Edit"}),

        To:
        Patch(colQuestionRow,ThisItem,{Edit: "Edit"}),
        
"""


def main(argv):
    pa_src_path = "example/src/*/Src/*.yaml"
    filenames = glob.glob(pa_src_path)

    for file in filenames:
        s = ""
        with open(file) as fin:
            s = fin.read()
        fin.close
        if 'UpdateIf' in s:
            print("******************************************************************************************************")
            print(f"Replace code in {file}:")
            print("******************************************************************************************************")

            copyfile(file, file + '.bak')
            with open(file) as fin:
                lines = fin.readlines()
            fin.close
            new_lines = []
            for line in lines:
                if 'UpdateIf' in line:
                    p = re.compile(
                        r'(?P<uif>UpdateIf)(?P<tab>.*?,)(?P<tim>.*?,)(?P<xxx>.*)')
                    n = p.sub(r'Patch\g<tab> ThisItem,\g<xxx>', line)
                    new_lines.append(n)
                    print(f'Old code {line}')
                    print(f'New code {n}')
                else:
                    new_lines.append(line)
            fout = open(file, "w")
            fout.writelines(new_lines)
            fout.close

    # run source-code replacing process

if __name__ == "__main__":
    main(sys.argv[1:])
