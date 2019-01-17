/**
 * @author syt123450 / https://github.com/syt123450
 */

const Utils = require( "./utils/Utils" );
const Converter = require( "./app/Converter" );
const Summary = require( "./app/Summary" );

let options = process.argv;

let output_layer_names = undefined;
let summary = false;
let hasOutputConfig = false;

for ( let i = 2; i <= options.length - 2; i ++ ) {

	let option = options[ i ];
	let parameters = option.split("=");

	if ( parameters[ 0 ] ===  "--output_layer_names" ) {

		hasOutputConfig = true;
		output_layer_names = Utils.getOutputLayerNames( parameters[ 1 ] );

	} else if ( parameters[ 0 ] === "--summary" ) {

		summary = true;

	}

}

if ( summary ) {

	Summary.showSummary(

		Utils.getInputPath( options[ options.length - 1 ] )

	);

} else {

	Converter.encapsulateModel(

		Utils.getInputPath( options[ options.length - 2 ] ),
		Utils.getOutputPath( options[ options.length - 1 ] ),
		output_layer_names,
		hasOutputConfig

	);

}