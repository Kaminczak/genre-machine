/* machine.js — the lever's state machine.
   Position 1 → 4 selects a story; pulling triggers the steam-burst shift. */

(function () {
  const data = window.GENRE_MACHINE_DATA;
  if (!data) {
    console.error('GENRE_MACHINE_DATA missing — check that data/stories.js loaded.');
    return;
  }

  const storyByPos = {};
  data.stories.forEach((s) => { storyByPos[s.lever_position] = s; });

  const detents = document.querySelectorAll('.detent');
  const leverArm = document.getElementById('lever-arm');
  const storyName = document.getElementById('story-name');
  const wallFrame = document.querySelector('.wall-frame');
  const audioLever = document.getElementById('audio-lever');
  const audioSteam = document.getElementById('audio-steam');
  const muteBtn = document.getElementById('mute-toggle');

  let currentPos = 1;
  let muted = true; /* default muted — many browsers block autoplay anyway */
  let shifting = false;

  /* ===== Lever position rendering ===== */

  function isVertical() {
    return window.matchMedia('(min-width: 901px)').matches;
  }

  function placeArm(pos) {
    const detent = document.querySelector(`.detent[data-position="${pos}"]`);
    if (!detent) return;
    const track = document.getElementById('lever-track');
    const trackRect = track.getBoundingClientRect();
    const detentRect = detent.getBoundingClientRect();
    if (isVertical()) {
      const offsetTop = detentRect.top - trackRect.top + (detentRect.height / 2) - (leverArm.offsetHeight / 2);
      leverArm.style.top = `${offsetTop}px`;
      leverArm.style.left = '';
    } else {
      const offsetLeft = detentRect.left - trackRect.left + (detentRect.width / 2) - (leverArm.offsetWidth / 2);
      leverArm.style.left = `${offsetLeft}px`;
      leverArm.style.top = '';
    }
  }

  function highlightDetent(pos) {
    detents.forEach((d) => {
      d.classList.toggle('active', parseInt(d.dataset.position, 10) === pos);
    });
    leverArm.setAttribute('aria-valuenow', pos);
    leverArm.setAttribute('aria-label', `Story selector, position ${pos} of 4`);
  }

  /* ===== Story switching ===== */

  function switchTo(pos, { initial = false } = {}) {
    if (shifting) return;
    if (pos < 1 || pos > 4) return;
    if (!initial && pos === currentPos) return;

    const story = storyByPos[pos];
    if (!story) return;

    shifting = !initial;
    currentPos = pos;
    highlightDetent(pos);
    placeArm(pos);

    if (initial) {
      Viewports.build(story, data.genres);
      storyName.textContent = story.title;
      return;
    }

    /* Animate */
    leverArm.classList.add('shifting');
    playSound(audioSteam);
    if (wallFrame) {
      const burst = document.createElement('div');
      burst.className = 'steam-burst';
      wallFrame.appendChild(burst);
      setTimeout(() => burst.remove(), 1000);
    }
    storyName.classList.add('shifting');

    Viewports.shift(story, data.genres, () => {
      storyName.textContent = story.title;
    });

    setTimeout(() => {
      leverArm.classList.remove('shifting');
      storyName.classList.remove('shifting');
      playSound(audioLever);
      shifting = false;
    }, 700);
  }

  function playSound(audio) {
    if (muted || !audio || !audio.src) return;
    try {
      audio.currentTime = 0;
      const p = audio.play();
      if (p && p.catch) p.catch(() => { /* autoplay blocked — silent fail */ });
    } catch (e) { /* ignore */ }
  }

  /* ===== Bindings ===== */

  detents.forEach((d) => {
    d.addEventListener('click', () => {
      const pos = parseInt(d.dataset.position, 10);
      switchTo(pos);
    });
  });

  /* Keyboard on the lever arm itself */
  leverArm.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
      e.preventDefault();
      switchTo(Math.min(4, currentPos + 1));
    } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
      e.preventDefault();
      switchTo(Math.max(1, currentPos - 1));
    } else if (e.key === 'Home') {
      e.preventDefault();
      switchTo(1);
    } else if (e.key === 'End') {
      e.preventDefault();
      switchTo(4);
    }
  });

  /* Click-drag on the lever (optional flavor): on mousedown, listen for move,
     snap to nearest detent on release */
  let dragging = false;
  let dragStart = null;

  leverArm.addEventListener('mousedown', (e) => {
    dragging = true;
    dragStart = { x: e.clientX, y: e.clientY, pos: currentPos };
    e.preventDefault();
  });
  leverArm.addEventListener('touchstart', (e) => {
    if (e.touches.length !== 1) return;
    dragging = true;
    dragStart = { x: e.touches[0].clientX, y: e.touches[0].clientY, pos: currentPos };
  }, { passive: true });

  function handleDragEnd(clientX, clientY) {
    if (!dragging) return;
    const dy = clientY - dragStart.y;
    const dx = clientX - dragStart.x;
    const stepSize = 80;
    let delta;
    if (isVertical()) {
      delta = Math.round(dy / stepSize);
    } else {
      delta = Math.round(dx / stepSize);
    }
    if (delta !== 0) {
      switchTo(Math.max(1, Math.min(4, dragStart.pos + delta)));
    }
    dragging = false;
  }

  document.addEventListener('mouseup', (e) => handleDragEnd(e.clientX, e.clientY));
  document.addEventListener('touchend', (e) => {
    if (e.changedTouches[0]) handleDragEnd(e.changedTouches[0].clientX, e.changedTouches[0].clientY);
  });

  /* Mute toggle */
  muteBtn.addEventListener('click', () => {
    muted = !muted;
    muteBtn.setAttribute('aria-pressed', muted ? 'false' : 'true');
    muteBtn.querySelector('.mute-icon').textContent = muted ? '\u{1F507}' : '\u{1F50A}';
  });
  /* default state — muted; the icon shows the muted glyph */
  muteBtn.setAttribute('aria-pressed', 'false');
  muteBtn.querySelector('.mute-icon').textContent = '\u{1F507}';

  /* Reposition arm on resize */
  window.addEventListener('resize', () => placeArm(currentPos));

  /* Initial paint — wait for fonts / layout */
  window.addEventListener('load', () => {
    switchTo(1, { initial: true });
    /* place arm once layout settles */
    setTimeout(() => placeArm(1), 50);
  });
})();
