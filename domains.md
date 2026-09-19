---
layout: default
title: Domains
permalink: /domains/
---

<h1>Domains</h1>
<p>Domains listed as detections by researchers across all binaries.
   <a href="{{ '/domains.csv' | relative_url }}" download>Download CSV</a></p>

<input id="filter" type="search" placeholder="Filter by domain or binary..." style="width:100%;max-width:420px;margin-bottom:1rem">

<table id="domains">
  <thead><tr><th>Domain</th><th>Binary</th></tr></thead>
  <tbody>
  {%- assign bins = site.lottunnels | sort: "Name" -%}
  {%- for b in bins -%}
    {%- for d in b.Detection -%}
      {%- if d.Domain -%}
    <tr>
      <td><code>{{ d.Domain | escape }}</code></td>
      <td><a href="{{ b.url | relative_url }}">{{ b.Name | escape }}</a></td>
    </tr>
      {%- endif -%}
    {%- endfor -%}
  {%- endfor -%}
  </tbody>
</table>

<script>
document.getElementById("filter").addEventListener("input", function (e) {
  var t = e.target.value.toLowerCase();
  Array.prototype.forEach.call(document.querySelectorAll("#domains tbody tr"), function (r) {
    r.style.display = r.textContent.toLowerCase().indexOf(t) > -1 ? "" : "none";
  });
});
</script>