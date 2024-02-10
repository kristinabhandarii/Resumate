//For one slider
// document.addEventListener("DOMContentLoaded", function() {
//     const slider = document.getElementById('skills');
//     const valueDisplay = document.querySelector('.value');

//     //Update the displayed value when the slider value changes
//     slider.addEventListener('input', function() {
//         valueDisplay.textContent = this.value;
//     });
// });


//For all while ensuring total sum=100
document.addEventListener("DOMContentLoaded", function() {
    const sliders = document.querySelectorAll('.slider');
    const values = document.querySelectorAll('.value');

    sliders.forEach((slider, index) => {
        slider.addEventListener('input', function() {
            // Calculate the remaining sum
            
            const currentSum = Array.from(sliders).reduce((sum, s, i) => (i !== index ? sum + parseInt(s.value, 10) : sum), 0);

            // Update the max values of all sliders to ensure the total sum is 100
            const remainingMax = 100 - currentSum;
            sliders.forEach(s => (s.max = remainingMax));

            // Update the displayed value
            values[index].textContent = this.value;
        });
    });
});
