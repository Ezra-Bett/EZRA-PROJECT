
function showSidebar(event){
    event.preventDefault(); // Prevents the page from scrolling to the top
    const sidebar = document.querySelector('.sidebar');
    sidebar.style.display = 'flex'; /* This makes the sidebar appear on clicking the menu icon */
}

function hideSidebar(event){
    event.preventDefault(); // Prevents the page from scrolling to the top
    const sidebar = document.querySelector('.sidebar');
    sidebar.style.display = 'none'; /* This makes the sidebar disappear on clicking the close icon */
    /* display : flex - show    none - not show */
}











