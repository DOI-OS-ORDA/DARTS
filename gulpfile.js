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

uswds.paths.dist.css = './dartstoo/dartstoo/static/css';
uswds.paths.dist.img = './dartstoo/dartstoo/static/img';
uswds.paths.dist.fonts = './dartstoo/dartstoo/static/fonts';
uswds.paths.dist.js = './dartstoo/dartstoo/static/js';
uswds.paths.dist.sass = './dartstoo/dartstoo/static/sass';

/**
 * Exports
 * Add as many as you need
 */

exports.init = uswds.init;
exports.compile = uswds.compile;
exports.copyAssets = uswds.copyAssets;