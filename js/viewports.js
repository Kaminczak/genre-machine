/* viewports.js — renders the 25-cell grid for the active story
   and handles the magnify-on-click overlay. */

const Viewports = (function () {
  const grid = document.getElementById('viewport-grid');
  const magnifier = document.getElementById('magnifier');
  const magImg = document.getElementById('magnifier-img');
  const magGenre = document.getElementById('magnifier-genre');
  const magLogline = document.getElementById('magnifier-logline');
  const magClose = document.getElementById('magnifier-close');

  function build(story, genres) {
    grid.innerHTML = '';
    genres.forEach((genre) => {
      const cell = document.createElement('button');
      cell.className = 'viewport';
      cell.type = 'button';
      cell.dataset.storyId = story.id;
      cell.dataset.genreId = genre.id;
      cell.setAttribute('aria-label', `${story.title} as ${genre.name}`);

      const filename = `${story.id}_${genre.id}_${genre.slug}.webp`;
      const logline = story.loglines[genre.id] || '';

      const img = document.createElement('img');
      img.className = 'viewport-img';
      img.alt = `${story.title} reimagined as ${genre.name}`;
      img.loading = 'lazy';
      img.src = `assets/images/${filename}`;
      img.onerror = function () {
        this.classList.add('missing');
      };

      const placeholder = document.createElement('div');
      placeholder.className = 'viewport-placeholder';
      placeholder.innerHTML = `
        <span class="ph-id">${genre.id}</span>
        <span class="ph-name">${genre.name}</span>
      `;

      const label = document.createElement('span');
      label.className = 'viewport-label';
      label.textContent = genre.name;

      cell.appendChild(img);
      cell.appendChild(placeholder);
      cell.appendChild(label);

      cell.addEventListener('click', () => {
        openMagnifier(story, genre, filename, logline);
      });

      grid.appendChild(cell);
    });
  }

  function openMagnifier(story, genre, filename, logline) {
    magImg.src = `assets/images/${filename}`;
    magImg.alt = `${story.title} reimagined as ${genre.name}`;
    magImg.onerror = function () {
      this.style.opacity = 0.15;
    };
    magImg.style.opacity = 1;
    magGenre.textContent = `${story.title} — ${genre.name}`;
    magLogline.textContent = logline;
    magnifier.classList.add('open');
    magnifier.setAttribute('aria-hidden', 'false');
  }

  function closeMagnifier() {
    magnifier.classList.remove('open');
    magnifier.setAttribute('aria-hidden', 'true');
  }

  /* Close on click outside the frame, ESC, or close button */
  magnifier.addEventListener('click', (e) => {
    if (e.target === magnifier) closeMagnifier();
  });
  magClose.addEventListener('click', closeMagnifier);
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMagnifier();
  });

  /* Shift transition — fade existing viewport images out, then rebuild */
  function shift(newStory, genres, onMid) {
    const imgs = grid.querySelectorAll('.viewport-img');
    imgs.forEach((img) => img.classList.add('shifting'));
    setTimeout(() => {
      build(newStory, genres);
      if (typeof onMid === 'function') onMid();
    }, 350);
  }

  return { build, shift, closeMagnifier };
})();
