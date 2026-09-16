const menu=document.querySelector('.menu'),links=document.querySelector('.links');
if(menu&&links){menu.addEventListener('click',()=>{links.classList.toggle('open');menu.classList.toggle('open')});links.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{links.classList.remove('open');menu.classList.remove('open')}))}
const observer=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting)e.target.classList.add('show')}),{threshold:.12});document.querySelectorAll('.reveal').forEach(e=>observer.observe(e));
