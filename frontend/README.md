<h1 align=center><strong>Frontend Application ⚡️</strong></h1>

## Qwik

I choose this java script framework for my frontend becuase of its crazy time complexity: $\math{O}(1)$. Yes, it's literally instant! This framework is quite young, please read more here:

- [Qwik Docs](https://qwik.builder.io/)
- [Vite](https://vitejs.dev/)

Before we start, create a directory named `coverage` in both `backend/` and `frontend/` for our testing reports. You don#t see them now because it is listed in `.gitignore`.

---

## PNPM

You will realize that I will only use the keyword `pnpm` for the frontend application. Read more about [PNPM](https://pnpm.io/). But, why use `pnpm`?

* Basicall `pnpm` = `npm` + `npx` on steroid that takes care ofsecurity vulnerabilities found in `npm` (I never ever need to delete that chatty GitHub bot's reminder that notifies me about the package vulnerability from`npm`!).
* `pnpm` is faster because it simply links files from the global sotre, while other copies files from its cache.

---

## Project Structure

This project is using Qwik with [QwikCity](https://qwik.builder.io/qwikcity/overview/). QwikCity is just a extra set of tools on top of Qwik to make it easier to build a full site, including directory-based routing, layouts, and more.

Inside your project, you'll see the following directory structure:

```
├── public/
│   └── ...
└── src/
    ├── components/
    │   └── ...
    └── routes/
        └── ...
```

- `src/routes`: Provides the directory based routing, which can include a hierarchy of `layout.tsx` layout files, and an `index.tsx` file as the page. Additionally, `index.ts` files are endpoints. Please see the [routing docs](https://qwik.builder.io/qwikcity/routing/overview/) for more info.

- `src/components`: Recommended directory for components.

- `public`: Any static assets, like images, can be placed in the public directory. Please see the [Vite public directory](https://vitejs.dev/guide/assets.html#the-public-directory) for more info.

---

## Add Integrations and Deployment

Use the `pnpm qwik add` command to add additional integrations. Some examples of integrations include: Cloudflare, Netlify or Express server, and the [Static Site Generator (SSG)](https://qwik.builder.io/qwikcity/static-site-generation/static-site-config/).

```shell
pnpm qwik add # or `yarn qwik add`
```

---

## Commands in Qwik with PNPM

Like any other frameworks, `Qwik` has its commands.

### Development

Development mode uses [Vite's development server](https://vitejs.dev/). During development, the `dev` command will server-side render (SSR) the output.

```shell
npm start # or `yarn start`
```

> Note: during dev mode, Vite may request a significant number of `.js` files. This does not represent a Qwik production build.

### Preview

The preview command will create a production build of the client modules, a production build of `src/entry.preview.tsx`, and run a local server. The preview server is only for convenience to locally preview a production build, and it should not be used as a production server.

```shell
pnpm preview # or `yarn preview`
```

### Production

The production build will generate client and server modules by running both client and server build commands. Additionally, the build command will use Typescript to run a type check on the source code.

```shell
pnpm build # or `yarn build`
```

### Linter

I use `ESLint` and `Prettier` with their `typescipt` plugin to lint for our Java Sctiptcode.
To utilize `ESLint`, run:

```shell
pnpm lint
```

To utilize `Prettier` for checking purpose, run:

```shell
pnpm fmt.check
```

To utilize `Prettier` for formatting our source code; run:

```shell
pnpm fmt
```

---

## Test

For testing our frontend application's soruce code, I chose [TS-Jest](https://kulshekhar.github.io/ts-jest/). To run the test, execute this command:

```shell
pnpm test
```

---
