console.log('hello word')

const url =window.location.href
const searchForm =document.getElementById('search-form')
const searchInput= document.getElementById('search-input')
const resultsBox=document.getElementById('results-box')

const csrf= document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData = (Hospital) => {
    $.ajax({
        type:'POST',
        url:'search_result/',
        data:{
            'csrfmiddlewaretoken':csrf,
            'hospital':hospital,
        },
        success:(res)=>{
            console.log(res)
        },
        error:(err)=>{
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup',e=>{
    console.log(e.target.value)

    // if (resultsBox.classList.getElementById('invisible')){
    //     resultsBox.classList.getElementById('invisible')
        

    // }
    if (resultsBox.classList.contains('invisible')){
        resultsBox.classList.remove('invisible')

    }

    sendSearchData(e.target.value)


})