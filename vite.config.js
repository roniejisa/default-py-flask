import { resolve } from "path";
import { defineConfig } from "vite";
const name = process.env.BUILD_TARGET;
// Parse command-line arguments

const plugins = {
    admin: {
        files: {
            css: [resolve(__dirname, "./resources/admin/scss/admin.scss")],
            js: [resolve(__dirname, "./resources/admin/js/admin.js")],
        },
        dir: resolve(__dirname, "./app/static/core/admin"),
    },
    login: {
        files: {
            css: [resolve(__dirname, "./resources/login/scss/login.scss")],
            js: [resolve(__dirname,"./resources/login/js/login.js")],
        },
        dir: resolve(__dirname, "./app/static/core/login"),
    },
    client: {
        files: {
            css: [],
            js: [resolve(__dirname,"./resources/client/js/script.js")],
        },
        dir: resolve(__dirname, "./app/static/core/client"),
    },
};

const getDir = (type) => {
    return plugins[type].dir;
};

const getFile = (type) => {
    return [...plugins[type].files.css, ...plugins[type].files.js];
};

export default defineConfig({
    build: {
        outDir: "./app/static/core",
        watch: true,
        copyPublicDir: false,
        chunkSizeWarningLimit: 2000,
        minify: true,
        rollupOptions: {
            input: getFile(name),
            output: {
                dir: getDir(name),
                entryFileNames: `js/[name].js`,
                chunkFileNames: `js/[name].js`,
                assetFileNames: `[ext]/[name].[ext]`,
            },
        },
    },
    server: {
        watch: {
            usePolling: true,
        },
    },
});
