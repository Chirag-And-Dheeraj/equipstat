let hamburger = document.getElementById('toggle_btn')
let sideNav = document.getElementById('SideNav')
let closeSideNav = document.getElementById('closeSideNav')

// console.log(hamburger);
// console.log(sideNav);
// console.log(closeSideNav);

hamburger.addEventListener('click', function(event){
    sideNav.style.marginLeft = "0px"
})

closeSideNav.addEventListener('click', function(event){
    sideNav.style.marginLeft = "-300px"
})

