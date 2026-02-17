document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const talkCards = document.querySelectorAll('.talk-card');
    const lunchBreak = document.querySelector('.lunch-break');
    const noResults = document.getElementById('noResults');

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        let visibleCount = 0;

        // Hide lunch break when searching
        if (query.length > 0) {
            if (lunchBreak) lunchBreak.style.display = 'none';
        } else {
            if (lunchBreak) lunchBreak.style.display = 'flex';
        }

        talkCards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            const category = card.dataset.category.toLowerCase();
            const speakers = Array.from(card.querySelectorAll('.speaker span'))
                                  .map(s => s.textContent.toLowerCase())
                                  .join(' ');
            
            if (title.includes(query) || category.includes(query) || speakers.includes(query)) {
                card.style.display = 'flex';
                // Add a small fade-in animation or just show
                card.style.opacity = '1';
                visibleCount++;
            } else {
                card.style.display = 'none';
                card.style.opacity = '0';
            }
        });

        // Show/Hide No Results
        if (visibleCount === 0 && query.length > 0) {
            noResults.classList.remove('hidden');
        } else {
            noResults.classList.add('hidden');
        }
    });

    // Add some simple entrance animations
    talkCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        setTimeout(() => {
            card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
});
