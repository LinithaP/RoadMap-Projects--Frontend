const fromUnit = document.getElementById('fromUnit')
const toUnit = document.getElementById('toUnit')
const tempInput = document.getElementById('value')
const resultMessage =document.getElementById('resultMessage')

function convert() {
    if (tempInput.value && fromUnit.value && toUnit.value) {
        displayResult();
    } else {
        resultMessage.textContent ='';
    }
};

function displayResult(){
    const temp = parseFloat(tempInput.value);
    const from = fromUnit.value;
    const to = toUnit.value;

    const result = convertValues(temp, from, to);
    resultMessage.textContent =`${temp} degree ${from}  is ${result} degree ${to} `;
};

function convertValues(temp, from, to) {
    let result;

    if (from === to) {
        return temp;
    };

    if (from === 'Celsius') {
        if (to === 'Fahrenheit') {
            result = (temp * 9/5) +32;
        } else if (to === 'Kelvin') {
            result = temp + 273.15;
        }
    }

    else if (from === 'Fahrenheit') {
        if (to === 'Celsius') {
            result = (temp - 32) * 5/9;
        } else if (to === 'Kelvin') {
            result = ((temp - 32) * 5/9) + 273.15;
        }
    }

    else if (from === 'Kelvin') {
        if (to === 'Fahrenheit') {
            result = ((temp - 273.15) * 9/5) + 32;
        } else if (to === 'Celsius') {
            result = temp - 273.15;
        }
    }

    return result;
};



function limitLength(input) {
    if (input.value.length > 4) {
      input.value = input.value.slice(0, 4);
    }
}



tempInput.addEventListener('input', convert);
fromUnit.addEventListener('change', convert);
toUnit.addEventListener('change', convert);