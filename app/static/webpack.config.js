const path = require('path')
const webpack = require('webpack')

const postCSSConfig = require('./src/postcss.config')
const srcPath = path.resolve(__dirname, 'src');


const OUTPUT_PATH = path.join(__dirname, 'build');

module.exports = {
    entry: {
        app: `${srcPath}/index.tsx`,
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
            { test: /\.tsx?$/, loader: "awesome-typescript-loader" },
            // {
            //     test: /\.css$/,
            //     loader: 'style!css?modules&importLoaders=1&localIdentName=[name]__[local]___[hash:base64:5]&camelCase!postcss'
            //   },

            { test: /\.css$/, loader: "style-loader!css-loader!postcss-loader" },
            // All output '.js' files will have any sourcemaps re-processed by 'source-map-loader'.
            // { enforce: "pre", test: /\.js$/, loader: "source-map-loader" }
        ]
    },
    // postcss: () => postCSSConfig,

    plugins: [
        new webpack.optimize.CommonsChunkPlugin({
            name: 'vendor'
        })
    ]
};