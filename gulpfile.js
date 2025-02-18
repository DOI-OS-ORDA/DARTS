const uswds = require("@uswds/compile");

/**
 * USWDS version
 * Set the version of USWDS you're using (2 or 3)
 */

uswds.settings.version = 3;

/**
 * Path settings
 * Set as many as you need
 */

uswds.paths.dist.css = './darts/darts/static/css';
uswds.paths.dist.img = './darts/darts/static/img';
uswds.paths.dist.fonts = './darts/darts/static/fonts';
uswds.paths.dist.js = './darts/darts/static/js';
uswds.paths.dist.sass = './darts/darts/static/sass';

/**
 * Exports
 * Add as many as you need
 */

exports.init = uswds.init;
exports.compile = uswds.compile;
exports.copyAssets = uswds.copyAssets;
