(() => {
  const root = document.documentElement;
  const system = window.matchMedia("(prefers-color-scheme: dark)");
  let preference;
  try {
    preference = localStorage.getItem("theme");
  } catch {
    // The control still works when browser storage is unavailable.
  }
  function apply() {
    const dark = preference === "dark" || (preference !== "light" && system.matches);
    root.setAttribute("data-theme", dark ? "dark" : "light");
    const button = document.querySelector(".theme-toggle");
    if (button) button.setAttribute("aria-pressed", String(dark));
  }
  apply();
  document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector(".theme-toggle");
    button.addEventListener("click", () => {
      preference = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      apply();
      try {
        localStorage.setItem("theme", preference);
      } catch {
        // Private browsing can limit persistence.
      }
    });
    apply();
    button.hidden = false;
  });
  system.addEventListener("change", apply);
})();
