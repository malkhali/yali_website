
function submitForm(e){
  e.preventDefault();
  const name = document.getElementById('name').value || 'Friend';
  document.getElementById('formResponse').style.display='block';
  document.getElementById('formResponse').innerText = `Thanks ${name}! We'll reach out soon.`;
  return false;
}

// Feature cards: reveal on scroll
document.addEventListener('DOMContentLoaded', function () {
  // reveal feature-card and cards inside .features
  const cards = Array.from(document.querySelectorAll('.feature-card'))
    .concat(Array.from(document.querySelectorAll('.features .card')));

  // staggered reveal for .service-small-card in .horizontal-row
  const serviceCards = Array.from(document.querySelectorAll('.horizontal-row .service-small-card'));
  serviceCards.forEach((c, i) => {
    c.classList.add('preview', `stagger-${i+1}`);
  });

  if (!('IntersectionObserver' in window)) {
    // fallback: reveal all
    cards.forEach(c => c.classList.add('in-view'));
    serviceCards.forEach(c => c.classList.add('in-view'));
    return;
  }

  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  cards.forEach(c => {
    c.classList.add('preview');
    io.observe(c);
  });
  serviceCards.forEach(c => {
    io.observe(c);
  });
});
