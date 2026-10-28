// Basic deterrents against casual image saving (not a real security measure,
// images remain fetchable via dev tools / network tab).
document.addEventListener("contextmenu", (e) => {
  if (e.target.tagName === "IMG") e.preventDefault();
});
document.addEventListener("dragstart", (e) => {
  if (e.target.tagName === "IMG") e.preventDefault();
});

const skillCards = document.querySelectorAll("#skills .card");
const mobileViewport = window.matchMedia("(max-width: 767px)");

if (skillCards.length && "IntersectionObserver" in window) {
  const skillCardObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        entry.target.classList.toggle(
          "active",
          mobileViewport.matches && entry.isIntersecting,
        );
      });
    },
    { rootMargin: "-35% 0px -35% 0px" },
  );

  const observeSkillCards = () => {
    skillCardObserver.disconnect();
    skillCards.forEach((card) => card.classList.remove("active"));

    if (mobileViewport.matches) {
      skillCards.forEach((card) => skillCardObserver.observe(card));
    }
  };

  observeSkillCards();
  mobileViewport.addEventListener("change", observeSkillCards);
}
