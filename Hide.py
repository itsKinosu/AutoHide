choice = ""
import os
txtfile = "hidelist.txt"
cwd = os.getcwd()
txtfileloc = os.path.join(cwd,txtfile)

if not os.path.exists(txtfileloc):

    with open(txtfileloc, "w") as f:

        f.write("Please put your folder/file locations to be hidden below:")
        f.flush()
        os.startfile(txtfileloc)
        _ = input("hidelist.txt has been created, please put your folder locations per line\nPress Enter to close")
        while _:
            break

else: 
    with open(txtfileloc, "r") as f:
        next(f)
        line2 = f.readline()

        if line2 == "":
            _ = input("Line 2 is blank or the file does not have any directory to hide\nPlease put in a directory to hide.\nPress Enter to close.")
            os.startfile(txtfileloc)
            while _:
                break

        elif line2 != "":

            while choice not in ["h","u", "k"]:
                choice = input("Select what you want to do:\n> H for hide\n> U for unhide\n> K for terminate program\n(Answer is Case Insensitive): ").lower()

                if choice.strip() == "k":
                    break

                elif choice.strip() == "h":
                    with open(txtfileloc, "r") as f:
                        next(f)
                        for line in f:
                            print(line)
                            os.system("attrib +h " + line)
                        _ = input("Directories are now hidden.\nPress Enter to terminate the program.")
                        while _:
                            break

                elif choice.strip() == "u":
                    with open(txtfileloc, "r") as f:
                        next(f)
                        for line in f:
                            print(line)
                            os.system("attrib -h " + line)
                        _ = input("Directories are now visible.\nPress Enter to terminate the program.")
                        while _:
                            break