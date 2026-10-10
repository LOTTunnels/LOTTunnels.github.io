---
layout: page
title: LOTTunnels
---

<script async src="https://www.googletagmanager.com/gtag/js?id=UA-133649096-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-133649096-1');
</script>

<div class="home-hero">
  <a href="https://github.com/LOTTunnels/LOTTunnels.github.io/blob/master/README.md">
    <img src="{{ '/assets/logo.png' | relative_url }}" alt="{{site.title}} Logo">
  </a>
  <div>
    <h2>Living Off The Tunnels</h2>
    <p>LOTTunnels is a community-driven project documenting digital tunneling tools and how they can be abused for data exfiltration, persistence, and shell access.</p>
    <nav class="home-actions" aria-label="Explore LOTTunnels">
      <a href="#binary-directory">Browse the catalog</a>
      <a href="{{ '/contributors/' | relative_url }}">Meet the contributors</a>
      <a href="https://lottunnels.github.io/domains.csv">Domains CSV</a>
      <a href="https://lottunnels.github.io/binaries.csv">Binaries CSV</a>
    </nav>
  </div>
</div>

<p class="home-note">Inspired by the <a href="https://lolbas-project.github.io/">LOLBAS project</a>. Thank you to everyone who contributes to the community.</p>

<section class="usage-section" aria-label="LOTTunnels references">
  <span class="usage-label">Featured in</span>
  <a class="usage-link" href="https://github.com/jeffreytigch/PreventKit" target="_blank" rel="noopener noreferrer">PreventKit ↗</a>
  <a class="usage-link" href="https://lnkd.in/p/dc8_H4Gy" target="_blank" rel="noopener noreferrer">MagicSword ↗</a>
</section>

[functions]: /functions/
<section id="binary-directory" aria-label="Binary catalog">
<h2>Explore the catalog</h2>
<p>Search binaries by name, function, or type.</p>
{% include bin_table.html %}
</section>
