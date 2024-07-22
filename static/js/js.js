try {
    const btn_copy = [...document.getElementsByClassName('btn_copy')];

    btn_copy.forEach(btn=>btn.addEventListener('click',()=>{
        const text = btn.value;
        navigator.clipboard.writeText(text);
    }))
}catch(err){
    console.log('');
}
try {
    let add = document.getElementById('add');
    let p = document.getElementById('p');

    add.onmouseover = ()=>{
        p.style.display = 'block';
        setTimeout(()=>{
            p.style.display = 'none';
        },1000);
    }
}catch(err){
    console.log('');
}