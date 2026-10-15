document.getElementById("year").textContent = new Date().getFullYear();
function escapeHTML(value) { return String(value ?? "").replace(/[&<>"']/g, ch => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch])); }
function formatDate(value) { if (!value) return "Date not provided"; const date = new Date(value); return Number.isNaN(date.getTime()) ? value : date.toLocaleDateString(undefined,{year:"numeric",month:"short",day:"numeric"}); }
async function loadNews() {
  const status=document.getElementById("news-status"), list=document.getElementById("news-list");
  try {
    const response=await fetch("./news.json?updated="+Date.now(),{cache:"no-store"});
    if(!response.ok) throw new Error("News file not available yet");
    const items=await response.json();
    if(!Array.isArray(items)||items.length===0) throw new Error("No items available yet");
    list.innerHTML=items.slice(0,12).map(item=>`<article class="news-card"><div class="date">${escapeHTML(formatDate(item.date))} · Official VA release</div><h3>${escapeHTML(item.title)}</h3><p>${escapeHTML(item.summary||"Open the official release for details.")}</p><a href="${escapeHTML(item.link)}" target="_blank" rel="noopener">Read original release ↗</a></article>`).join("");
    status.textContent="Showing "+Math.min(items.length,12)+" recent items from the official VA news-release feed.";
  } catch(error) {
    status.textContent="The automated feed has not run successfully yet. Please check back soon, or visit the official VA Press Room directly.";
    list.innerHTML='<p><a href="https://news.va.gov/va-press-room/" target="_blank" rel="noopener">Open the official VA Press Room ↗</a></p>';
  }
}
loadNews();
