<h1 align=center><strong>Frontend Application 🧬</strong></h1>

## React

I chose React JS + TypeScript because they are the industry standard for frontend development,but yet quite easy to start with. Please read more about them here:

- [React JS](https://reactjs.org/)
- [TypeScript](https://www.typescriptlang.org/)

Before we start, create a directory named `coverage` in both `backend/` and `frontend/` for our testing reports. You don#t see them now because it is listed in `.gitignore`.

---

## PNPM

You will realize that I will only use the keyword `pnpm` for the frontend application. Read more about [PNPM](https://pnpm.io/). But, why use `pnpm`?

* Basicall `pnpm` = `npm` + `npx` on steroid that takes care ofsecurity vulnerabilities found in `npm` (I never ever need to delete that chatty GitHub bot's reminder that notifies me about the package vulnerability from`npm`!).
* `pnpm` is faster because it simply links files from the global store, while other copies files from its cache (no need to understand what global store is for now 😉).

---

## Project Structure

Inside your project, you'll see the following directory structure:

```shell
frontned/
├── coverage/           # Test reports
├── public/             # Static assets (JSON, SVG, TXT files)
│   └── ...
├── src/                # The main frontend application source code
    ├── components/     # Components storage
        ├── ...
    ├── routes/         # Enpoint routes
        ├── ...
├── .eslintrc.json      # ESLint (linting) configuration file
├── .npmrc              # PNPM/NPM configuratin file
├── .prettierrc.json    # Prettier-configuration file
├── jest.config.js      # JEST (testing) configuration file
├── package.json        # Package-related confugiration file
├── pnpm-lock.yaml      # Locked packages with the version installed for frontend app
├── README.md           # Documentation file for frontend app
├── tsconfig.json       # TypeScript-related configuration file
```

---

## Important Commands with PNPM

The commands are more or less the same ones between `npm`, `npx`, `yarn`, and `pnpm`.

* Run Development Server

    ```shell
    pnpm start
    ```


* Run in Production

    The production build will generate client and server modules by running both client and server build commands. Additionally, the build command will use Typescript to run a type check on the source code.

    ```shell
    pnpm build
    ```

* Run Linter

    I use `ESLint` and `Prettier` with their `typescipt` plugin to lint and format our Java Script code. To utilize `ESLint`, run:

    * Inspection only with `Prettier`

        ```shell
        pnpm lint:check
        ```

    * Inspection + fixing the code with `Prettier`

        ```shell
        pnpm lint:fix
        ```

    * Inspection only with `ESLint`

        ```shell
        pnpm fmt:check
        ```

    * Inspection + fixing the code with `ESLint`

        ```shell
        pnpm fmt:fix
        ```

---

## Run Test

For testing our frontend application's soruce code, I chose [TS-Jest](https://kulshekhar.github.io/ts-jest/). Even though the test is set up, as a beginner, I sometimes don't want to test my application right away. This is no problem! Because I set up the test with the extra argument `--passWithNoTests` which still lets you test your code, but also passes the test **IF** you are too lazy to write a test. This approach might be useful for you, if you want to learn CI/CD 😉

* Test, but pass the test without any test code:

    ```shell
    pnpm test:notestpass
    ```

* Test:

    ```shell
    pnpm test
    ```

---

## What's Next?

Next, we you will see how I set up the `Docker` container! Click [here](https://github.com/Aeternalis-Ingenium/DAPSQL-FART-Stack-Template/trunk/CONTAINER.md)
