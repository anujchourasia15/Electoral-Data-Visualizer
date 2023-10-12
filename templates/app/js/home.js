const stateData = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha (formerly Orissa)",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
];

const cityData = {
    "Madhya Pradesh": [
        "Bhopal (Capital city)",
        "Indore",
        "Jabalpur",
        "Gwalior",
        "Ujjain",
        "Sagar",
        "Dewas",
        "Satna",
        "Ratlam",
        "Rewa",
        "Katni",
        "Burhanpur",
        "Chhindwara",
        "Damoh",
        "Shivpuri",
        "Mandsaur",
        "Neemuch",
        "Vidisha",
        "Hoshangabad",
        "Itarsi",
        "Betul",
        "Seoni",
        "Khandwa",
        "Khargone",
        "Morena",
        "Balaghat",
        "Singrauli",
        "Shahdol",
        "Narsinghpur",
        "Sehore",
        "Harda",
        "Panna",
        "Chhatarpur",
        "Rajgarh",
        "Datia",
        "Anuppur",
        "Guna",
        "Ashoknagar",
        "Dhar",
        "Agar Malwa",
        "Shajapur",
        "Raisen",
        "Tikamgarh",
        "Sheopur",
        "Mandla",
        "Dindori",
        "Alirajpur",
        "Niwari"
    ],
    // Add cities for other states here
};

const tehsilData = {
    // Add tehsils for each city here
    "Indore": [
        "INDORE",
    ],
    "Bhopal (Capital city)": [
        "GOVINDPURA",
    ]
};


const stateSelect = document.getElementById("state-select");
const citySelect = document.getElementById("city-select");
const tehsilSelect = document.getElementById("tehsil-select");
const villageSelect = document.getElementById("village-select");

// Populate the state dropdown with options
stateData.forEach(state => {
    const optionElement = document.createElement("option");
    optionElement.value = state;
    optionElement.textContent = state;
    stateSelect.appendChild(optionElement);
});

stateSelect.addEventListener("change", function () {
    const selectedState = stateSelect.value;
    const cities = cityData[selectedState] || [];
    populateDropdown(citySelect, cities);
    clearDropdowns(tehsilSelect, villageSelect);
});

citySelect.addEventListener("change", function () {
    const selectedCity = citySelect.value;
    const tehsils = tehsilData[selectedCity] || [];
    populateDropdown(tehsilSelect, tehsils);
    clearDropdown(villageSelect);
});

tehsilSelect.addEventListener("change", function () {
    const selectedTehsil = tehsilSelect.value;
    const villages = villageData[selectedTehsil] || [];
    populateDropdown(villageSelect, villages);
});

function populateDropdown(dropdown, options) {
    // Clear the dropdown first
    clearDropdown(dropdown);

    // Add new options
    options.forEach(option => {
        const optionElement = document.createElement("option");
        optionElement.value = option;
        optionElement.textContent = option;
        dropdown.appendChild(optionElement);
    });
}

function clearDropdown(dropdown) {
    dropdown.innerHTML = '<option value="">Select an option</option>';
}

function clearDropdowns(...dropdowns) {
    dropdowns.forEach(dropdown => clearDropdown(dropdown));
}
