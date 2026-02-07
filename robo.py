import os

print("Hiiii there! I am your Robospeaker ")
print("Type something and i will speak it . Type 'exit' to quit.")
while True:
    x = input("Enter what you want to say hii: ")
    if x.lower() == "exit":
        print("Goodbye!")
        break
    if x.strip() == "":
        continue  # ignore empty input
    # this line makes windows speak your text 
    os.system(f'powershell -Command "Add-Type –AssemblyName System.Speech; '
              f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
              f'$speak.Speak(\'{x}\');"')
