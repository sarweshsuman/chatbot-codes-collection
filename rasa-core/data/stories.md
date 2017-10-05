## story_001
* _greet
   - action_greet
* _product_information[software_name=hss,software_version=6.0,whatisrequired=hardware]
   - action_save_to_slots
   - action_product_information

## story_003
* _greet
   - action_greet
* _product_information
   - action_product_information

## story_002
* _product_information[software_name=hss,software_version=6.0,whatisrequired=hardware]
   - action_save_to_slots
   - action_product_information

## story_004
* _product_information
   - action_product_information

## story_101
* _greet
   - action_greet
* _product_deployment[software_name=hss,software_version=6.0,source_location=/home/id832037,destination_location=tomcat]
   - action_save_to_slots
   - action_product_deployment

## story_103
* _greet
   - action_greet
* _product_deployment
   - action_product_deployment

## story_102
* _product_deployment[software_name=hss,software_version=6.0,source_location=/home/id832037,destination_location=tomcat]
   - action_save_to_slots
   - action_product_deployment

## story_104
* _product_deployment
   - action_product_deployment

## story_201
* _update_slots
   - action_save_to_slots
   - action_updated_slots
