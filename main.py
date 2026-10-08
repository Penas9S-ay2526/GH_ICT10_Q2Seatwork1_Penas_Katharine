from pyscript import display, document

def generate(e): #identification of variables
    country1 = document.getElementById("GB")
    country2 = document.getElementById("DE")
    country3= document.getElementById("FR")
    country4= document.getElementById("FI")
    country5 = document.getElementById("AT")
    country6 = document.getElementById("IS")

    nickname = (country1.value) * country1.selected + (country2.value) * country2.selected + (country3.value) * country3.selected + (country4.value) * country4.selected + (country5.value) * country5.selected + (country6.value) * country6.selected
    


    display(f'The nickname of that country is "{nickname}"!', target='result', append=False)