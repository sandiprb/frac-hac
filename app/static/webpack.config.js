const path = require('path')
const webpack = require('webpack')

const OUTPUT_PATH = path.join(__dirname, 'build');

module.exports = {
    entry: {
        app: "./js/index.tsx",
        vendor: ["react", "react-dom"],
    },

    output: {
        path: OUTPUT_PATH,
        // filename: '[name].[hash].bundle.js',
        filename: '[name].bundle.js',
        // chunkFilename: '[name].bundle.js',
    },


    resolve: {
        extensions: [".ts", ".tsx", ".js", ".json"]
    },

    module: {
        rules: [
            // All files with a '.ts' or '.tsx' extension will be handled by 'awesome-typescript-loader'.
            { test: /\.tsx?$/, loader: "awesome-typescript-loader" },

            // All output '.js' files will have any sourcemaps re-processed by 'source-map-loader'.
            { enforce: "pre", test: /\.js$/, loader: "source-map-loader" }
        ]
    },

    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
            name: 'vendor'
        })
    ]
};