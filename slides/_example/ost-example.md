---
theme: ost
paginate: true
marp: true
html: true
title: "Marp OST Theme Example"
header: "Marp OST Theme Example"
footer: "Timon Erhart &nbsp;| &nbsp; [OST Ostschweizer Fachhochschule](https://www.ost.ch)"
backgroundImage: ../theme/image1.jpg
---

<!-- _class: lead -->
<!-- _paginate: skip # skip the header -->
<!-- _header: "" # skip the footer -->
<!-- _footer: "" # skip the footer -->

<style scoped>
  * {
    background-color: rgba(255, 255, 255, 0.3);
  }
</style>

![bg cover](../theme/image2.jpg)

# Marp OST Theme Example

Timon Erhart

---

# Title
## Subtitle
### Sektion

Normal text **bold text** *italic text*

[Link](https://www.ost.ch)

`inline code`

<mark>highlighted text</mark>

<mark class="good">highlighted text (good)</mark>

<mark class="bad">highlighted text (bad)</mark>

---

## Lists

- Unordered list item 1
- Unordered list item 2
- Unordered list item 3

1. Ordered list item 1
2. Ordered list item 2
3. Ordered list item 3

---

## Other elements

> Blockquote
> Lorem ipsum

```python
# Code block
def hello():
    print("Hello, World!")
```

---

## Tables

| Header 1    | Header 2    | Header 3    |
| ----------- | ----------- | ----------- |
| Row 1 Col 1 | Row 1 Col 2 | Row 1 Col 3 |
| Row 2 Col 1 | Row 2 Col 2 | Row 2 Col 3 |
| Row 3 Col 1 | Row 3 Col 2 | Row 3 Col 3 |

---

## Columns

<div class="columns">
  <div class="column">

### Left column

- Item 1
- Item 2
- Item 3

  </div>
  <div class="column">

### Right column

- Item A
- Item B
- Item C

  </div>

---

## Boxes

<div class="boxes">
  <div class="box">

### Left box

- Item 1
- Item 2
- Item 3

  </div>
  <div class="box">

### Right box

- Item A
- Item B
- Item C

  </div>
</div>

---

## Cards

<div class="cards">
  <div class="card">
    <span class="logo">🚀</span>
    <div>

### Emoji logo

Short text next to an emoji logo.

   </div>
  </div>
  <div class="card">
    <img src="../theme/open-ost_logo.svg" alt="">
    <div>

### SVG logo

Short text next to an SVG logo.

   </div>
  </div>
</div>

---

# Breaker

![bg left:50%](https://picsum.photos/720?image=29)

---

![bg cover opacity:0.3](../theme/image2.jpg)

# Soft Background

- Item 1
- Item 2
- Item 3