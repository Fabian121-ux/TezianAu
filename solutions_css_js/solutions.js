document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.solution-card');
    
    cards.forEach((card, index) => {
        card.style.setProperty('--animation-order', index);
        
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) rotateY(10deg)';
            this.style.boxShadow = '0 8px 12px rgba(0, 0, 0, 0.15)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) rotateY(0)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        });
    });

    // Add parallax effect to cards on mouse move
    document.addEventListener('mousemove', function(e) {
        const mouseX = e.clientX;
        const mouseY = e.clientY;
        
        cards.forEach(card => {
            const rect = card.getBoundingClientRect();
            const cardX = rect.left + rect.width / 2;
            const cardY = rect.top + rect.height / 2;
            
            const angleX = (mouseY - cardY) / 30;
            const angleY = (mouseX - cardX) / -30;
            
            card.style.transform = `rotateX(${angleX}deg) rotateY(${angleY}deg)`;
        });
    });
});
