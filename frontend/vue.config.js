module.exports = {
  configureWebpack: {
    devServer: {
      watchOptions: {
        ignored: ['node_modules'],
        aggregateTimeout: 300,
        poll: 1500
      }
    },
    devtool: 'source-map'
  }
}
