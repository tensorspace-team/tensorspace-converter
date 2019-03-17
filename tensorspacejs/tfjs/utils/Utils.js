/**
 * @author syt123450 / https://github.com/syt123450
 */

function getInputPath( path ) {

	return 'file://' + path;

}

function getOutputPath( path ) {

	return 'file://' + path;

}

function getOutputLayerNames( names ) {

	let output_layer_names = [];
	let nameInArray = names.split(',');

	for ( let i = 0; i < nameInArray.length; i ++ ) {

		output_layer_names.push( nameInArray[ i ] );

	}

	return output_layer_names;

}

exports.getInputPath = getInputPath;
exports.getOutputPath = getOutputPath;
exports.getOutputLayerNames = getOutputLayerNames;