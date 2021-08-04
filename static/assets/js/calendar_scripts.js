$('.ui.dropdown').dropdown({
    forceSelection: false
});


const yearDataBox = document.getElementById('year-data-box')
const yearInput = document.getElementById('years')

$.ajax({
    type: 'GET',
    url: 'year-json',
    success: function(response){
        const yearData = response.data

        yearData.map(item=>{
            const option = document.createElement('div')
            option.textContent = item.name
            option.setAttribute('class', 'item')
            option.setAttribute('data-value', item.name)
            yearDataBox.appendChild(option)

        })
    },
    error: function(error){
        console.log(error)
    }
})

const monthDataBox = document.getElementById('month-data-box')
const monthInput = document.getElementById('months')
const monthHiddenInput = document.getElementById('month-hidden')
const monthText = document.getElementById('month-text')

yearInput.addEventListener('change', e=>{
    const selectedYear = e.target.value

    monthDataBox.innerHTML = ""
    monthHiddenInput.setAttribute('value', '')
    monthText.textContent = 'Month'
    monthText.classList.add('default')

    dayDataBox.innerHTML = ""
    dayHiddenInput.setAttribute('value', '')
    dayText.textContent = 'Day'
    dayText.classList.add('default')

    timeDataBox.innerHTML = ""
    timeText.textContent = 'Time'
    timeText.classList.add('default')

    $.ajax({
        type: 'GET',
        url: `month-json/${selectedYear}/`,
        success: function(response){
            console.log(response.data)
            const monthData = response.data
            monthData.map(item=>{
                const option = document.createElement('div')
                option.textContent = item.name
                option.setAttribute('class', 'item')
                option.setAttribute('data-value', item.name)
                monthDataBox.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})

const dayDataBox = document.getElementById('day-data-box')
const dayInput = document.getElementById('days')
const dayHiddenInput = document.getElementById('day-hidden')
const dayText = document.getElementById('day-text')


monthInput.addEventListener('change', e=>{
    const selectedMonth = e.target.value

    dayDataBox.innerHTML = ""
    dayHiddenInput.setAttribute('value', '')
    dayText.textContent = 'Day'
    dayText.classList.add('default')

    timeDataBox.innerHTML = ""
    timeHiddenInput.setAttribute('value', '')
    timeText.textContent = 'Time'
    timeText.classList.add('default')

    $.ajax({
        type: 'GET',
        url: `day-json/${selectedMonth}/`,
        success: function(response){
            console.log(response.data)
            const dayData = response.data
            dayData.map(item=>{
                const option = document.createElement('div')
                option.textContent = item.name
                option.setAttribute('class', 'item')
                option.setAttribute('data-value', item.date)
                dayDataBox.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})

const timeDataBox = document.getElementById('time-data-box')
const timeHiddenInput = document.getElementById('time-hidden')
const timeInput = document.getElementById('times')
const timeText = document.getElementById('time-text')
const btnSubmit = document.getElementById('btn-submit')

dayInput.addEventListener('change', e=>{
    const selectedDay = e.target.value

    timeDataBox.innerHTML = ""
    timeText.textContent = 'Time'
    timeText.classList.add('default')

    $.ajax({
        type: 'GET',
        url: `time-json/${selectedDay}/`,
        success: function(response){
            console.log(response.data)
            const timeData = response.data
            timeData.map(item=>{
                const option = document.createElement('div')
                option.textContent = item.name
                option.setAttribute('class', 'item')
                option.setAttribute('data-value', item.name)
                timeDataBox.appendChild(option)
            })

            timeInput.addEventListener('change', e=>{
                btnSubmit.removeAttribute('hidden')
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})



