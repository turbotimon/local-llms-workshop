---
theme: gaia
# class: lead
paginate: true
marp: true

# Header and footer can include markdown (even images) as well as HTML. Wrap in quotes to avoid parsing issues.
header: "**Header** – Can use *markdown*, even images ![opacity:.3](https://picsum.photos/id/63/32/32)"
footer: '<span style="color: #8495ab;">This is the footer</span>'
---

<!-- _paginate: skip-->
<!-- _class: lead -->

# Marp

- [Marp](https://marp.app/) Quick Start

---

## Directives

- Either in the front matter
  - Use single or double quotes to avoid parsing issues
- Or in the slides as HTML comments
    - For all slides `<!-- paginate: true -->`
    - Prefix with `_` only for this slide: `<!-- _paginate: skip -->`
- See https://marpit.marp.app/directives

Example: `<!-- _header: "Special header just for this slide" -->`
<!-- _header: "Special header just for this slide" -->

---

## Classes

At the some page, you might think want to change the layout, theme color, and so on. class local directive can change a class attribute of `<section>` element of slide page.

```md
<!-- _class: lead -->
```

Then, you can use CSS to style it:

```css
section.lead h1 {
  text-align: center;
}
```

---

## Speaker Notes

- All HTML comments (other than directives) are treated as speaker notes

```html
<!-- This is a speaker note -->
```

<!-- This is a speaker note -->

---

## Fragmented list

When using `*` or `-` for bullet lists, you can add the `fragment` class to make them appear **one by one in HTML presentation**:


* One
* Two
* Three

For ordered list, fragmentation is enabled by using `)` instead of `.`:

1) One
2) Two
3) Three

---

## Background directives

<!-- _backgroundImage: "linear-gradient(to bottom, #67b8e3, #0288d1)" -->

- Gradient background: `<!-- _backgroundImage: "linear-gradient(to bottom, #67b8e3, #0288d1)" -->`
  - Remember, use `_` prefix to apply the directive only for this slide
- Other directives:
  - `backgroundColor`
  - `backgroundImage`
  - `backgroundPosition` (center by default)
  - `backgroundRepeat` (no-repeat by default)
  - `backgroundSize` (cover by default)
  - `color`

---

## Images and Background syntax

Images can use special syntax:https://marpit.marp.app/image-syntax?id=resizing-image

- Size: `![w:32 h:32](image.jpg)`
- CSS filters: `![blur:10px](image.jpg)`
  - Other filters: `brightness:1.5`, `contrast:200%`, `grayscale:1`, `drop-shadow:0,5px,10px,rgba(0,0,0,.4)`, `opacity:.5`, ...
- Background: `![bg <optional_size_keyword>](image.jpg)`
  - Other size keywords: `cover`, `contain`, `fit`, `auto`, `80%`, `left`, ...

---

![bg left:33%](https://picsum.photos/720?image=27)

## Images and Background syntax (example)

- Example of background image to the left with 33% width

---

## Tweak style (Global)

- Marpit gives the `<style>` HTML element written in Markdown a special treatment. It will be converted to theme and bundle to the converted CSS.

```md
<style>
section {
  background: yellow;
}
</style>
```

- Or use the global directive in front matter_

```md
theme: base-theme
style: |
  section {
    background-color: #ccc;
  }
```

---

## Tweak style (Scoped)

We also support the scoped inline style through `<style scoped>`:

```md
<style scoped>
section {
  color: blue;
}
</style>
```

<style scoped>
section {
  color: blue;
}
</style>

---

<!-- _class: lead -->

# Examples

----

## Two columns example (flexbox)

<div style="display: flex; gap: 20px;">
<div style="flex: 0.5; border: 1px solid #ccc;">

### Box 1

</div>
<div style="flex: 1; border: 1px solid #ccc;">

### Box 2
Content here

</div>
</div>

---

## Two columns example (grid, RAW)

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
  <div style="border: 1px solid #ccc; padding: 20px;">
    **Box 1**
    Content here
  </div>
  <div style="border: 1px solid #ccc; padding: 20px;">
    **Box 2**
    Content here
  </div>

</div>

## Four 2x2 example (grid, RAW)

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
  <div style="padding: 20px; border-radius: 20px; background: #f0f0f0;">Row 1, Col 1</div>
  <div style="padding: 20px; border-radius: 20px; background: #f0f0f0;">Row 1, Col 2</div>
  <div style="padding: 20px; border-radius: 20px; background: #f0f0f0;">Row 2, Col 1</div>
  <div style="padding: 20px; border-radius: 20px; background: #f0f0f0;">Row 2, Col 2</div>
</div>

---

<style scoped>
section > two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}
section > three-col {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 20px;
}
section > two-col > div,
section > three-col > div {
  border: 1px solid #ccc;
  padding: 20px;
}
</style>

## Two columns example with CSS

<two-col>
  <div>

  - With empty line before/after the `<div>` tag, the content will be parsed as **Markdown**.
  - Lorem ipsum dolor sit amet.

  </div>
  <div>

  - Lorem ipsum dolor sit amet.
    - Lorem ipsum dolor sit amet.

  </div>
</div>
