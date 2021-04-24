// accordian animations - start - sm

const accBtns = document.querySelectorAll('.btn')
const chevronArrow = document.querySelectorAll('.chevron')

if(innerWidth < 768) {
    const btns = [...accBtns]
    const btnsState = btns.map( btn => ({btn, closed:null}))

    for (let i = 0; i < accBtns.length; i++) {
        let panel = accBtns[i].nextElementSibling
        let childElements = Array.from(accBtns[i].children)
        btnsState[i].btn.addEventListener('click', e => {
            
            //close accordian if any other accordian is open and rotate chevron
            for (let j = 0; j < accBtns.length; j++) {
                btnsState[j].closed = false
                if(accBtns[j].nextElementSibling.classList.contains('opened')) {
                    accBtns[j].nextElementSibling.style.maxHeight = null
                    btnsState[j].closed = true
                    accBtns[j].nextElementSibling.classList.remove('opened')
                    Array.from(accBtns[j].children)[1].classList.remove("transform", "-rotate-180")
                }
            }

            //open accordian and rotate chevron
            if(btnsState[i].closed !== true){
                panel.style.maxHeight = `${panel.scrollHeight}px`;
                panel.classList.add('opened')
                childElements[1].classList.add("transition-all", "transform", "rotate-180")
            }
        })
    }
}
// accordian animations - end - sm


let file = null
let image = document.querySelector('.includes-dd #image')
const validFileExtensions = [...image.getAttribute('accept').split(',')]
const uploadedImages = document.querySelector('.includes-dd .uploaded-images')
if(innerWidth >= 768) {
    //accordian chevron arrows back to normal
    chevronArrow.forEach(arrow => arrow.classList.add("transform", "-rotate-90"))

    // drag and drop start
    const dropArea = document.querySelector('.includes-dd .drag-area')

    // when a file is dragging over drag-area
    dropArea.addEventListener('dragover', e => {
        e.preventDefault()
        dropArea.children[0].children[0].classList.add('animate-bounce')
    })

    // when a file dragged over drag-area was left
    dropArea.addEventListener('dragleave', e => {
        dropArea.children[0].children[0].classList.remove('animate-bounce')
    })

    // when a file is dropped in drag-area
    dropArea.addEventListener('drop', e => {
        e.preventDefault()
        dropArea.children[0].children[0].classList.remove('animate-bounce')
        file = e.dataTransfer.files[0]
        let list = new DataTransfer()
        for(let file of e.dataTransfer.files){
            list.items.add(file)
        }
        let myFileList = list.files
        image.files = myFileList
        console.log(image.files)
        if(validFileExtensions.includes(file.type)){
            fileReader.onload = () => {  //this event is fired when read from file is over
                let fileUrl = fileReader.result
                let imgTag = `<img src="${fileUrl}" width="50" height="50" alt="" title="">`
                uploadedImages.innerHTML = imgTag
                uploadedImages.classList.remove("hidden")
                uploadedImages.classList.add("block")
            }
            fileReader.readAsDataURL(file) //asynchronous call to read data from file
        }else{
            console.log("This is Invalid as it is not an Image file", file)
        }
    })
}
