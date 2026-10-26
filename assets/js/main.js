// Basic deterrents against casual image saving (not a real security measure,
// images remain fetchable via dev tools / network tab).
document.addEventListener("contextmenu", (e) => {
  if (e.target.tagName === "IMG") e.preventDefault();
});
document.addEventListener("dragstart", (e) => {
  if (e.target.tagName === "IMG") e.preventDefault();
});
