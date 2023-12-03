import subprocess

# Run 'pip list' command to get installed packages
result = subprocess.run(['pip', 'list'], capture_output=True, text=True)

# Get the installed packages output
installed_packages = result.stdout

# Write the installed packages to a text file
with open('installed_packages.txt', 'w') as file:
    file.write(installed_packages)

print('Installed packages saved to "installed_packages.txt"')
