# Q 0 : # @country.states.accessible_by(current_ability).order("name ASC")
Query(Country)
.order('name')
# Q 1 : # @current_api_user.spree_roles.pluck(:name)
# Q 2 : # @customer_return.reimbursements.select(&:pending?)
Query(Reimbursement)
.where("customer_return_id = ?")
.select('pending?')
# Q 3 : # @order.all_adjustments.eligible.order(created_at: :asc)
Query(Order)
.where("order_id = ?")
.where("id = ?")
# Q 4 : # @order.payments.find_by!(number: params[:id])
Query(Payment)
.where("order_id = ?")
.where("number = ?")
# Q 5 : # @order.payments.find_by!(number: params[:payment_id])
Query(Payment)
.where("order_id = ?")
.where("number = ?")
# Q 6 : # @order.payments.includes(refunds: :reason)
Query(Payment)
.where("order_id = ?")
# Q 7 : # @order.state_changes.includes(:user).order(created_at: :desc)
Query(StateChange)
.where("order_id = ?")
.includes('user')
.order('created_at')
# Q 8 : # @payment.payment_method.payment_source_class.find_by(id: params[:card])
Query(PaymentMethod)
.where("id = ?")
.where("id = ?")
# Q 9 : # @payment_methods.find
Query(PaymentMethod)
.where("id = ?")
# Q 10 : # @product.product_properties.find_by(id: params[:id])
Query(Product)
.where("id = ?")
# Q 11 : # @product.product_properties.includes(:property).where(spree_properties: { name: params[:id] }).first
Query(Product)
.where("name = ?")
.return_limit('1')
# Q 12 : # @products.includes(:variants_including_master, variant_images: :viewable).friendly.distinct(false).find(params[:id])
Query(Product)
.distinct('')
.where("id = ?")
# Q 13 : # @products.where("spree_prices.amount IS NOT NULL").where("spree_prices.currency" => current_currency)
Query(Product)
.where("currency" = ?")
# Q 14 : # @promotion.promotion_actions.find(params[:id])
Query(PromotionAction)
.where("promotion_id = ?")
.where("id = ?")
# Q 15 : # @promotion.promotion_rules.find(params[:id])
Query(PromotionRule)
.where("promotion_id = ?")
.where("id = ?")
# Q 16 : # @properties.where(id: params[:ids].split(",").flatten)
Query(Property)
.where("id = ?")
# Q 17 : # @stock_location.stock_items.accessible_by(current_ability, :show).includes(includes)
Query(StockItem)
.where("stock_location_id = ?")
# Q 18 : # @taxonomy.taxons.find(params[:id])
Query(Taxon)
.where("taxonomy_id = ?")
.where("id = ?")
# Q 19 : # @updating_params[:order][:payments_attributes].first
# Q 20 : # @updating_params[:order][:payments_attributes].first
# Q 21 : # @user.store_credits.find(params[:id])
Query(User)
.where("id = ?")
# Q 22 : # Adjustment.eligible.promotion.where(source_id: actions.map(&:id))
Query(Adjustment)
.where("source_id = ?")
# Q 23 : # Country.accessible_by(current_ability, :show).find(params[:country_id])
Query(Country)
.where("id = ?")
# Q 24 : # Country.accessible_by(current_ability, :show).find(params[:id])
Query(Country)
.where("id = ?")
# Q 25 : # Country.order("updated_at ASC").last
Query(Country)
.order('updated_at')
.return_limit('1')
# Q 26 : # Country.order(:name)
Query(Country)
.order('name')
# Q 27 : # Country.order(:name)
Query(Country)
.order('name')
# Q 28 : # CreditCard.find_by(gateway_customer_profile_id: random)
Query(CreditCard)
.where("gateway_customer_profile_id = ?")
# Q 29 : # CreditCard.where(id: credit_card_ids)
Query(CreditCard)
.where("id = ?")
# Q 30 : # CreditCard.where(id: credit_card_ids)
Query(CreditCard)
.where("id = ?")
# Q 31 : # CustomerReturn.find(params[:build_from_customer_return_id])
Query(CustomerReturn)
.where("id = ?")
# Q 32 : # Doorkeeper::AccessToken.active_for(user).last
# Q 33 : # Image.accessible_by(current_ability, :show).find(params[:id])
Query(Image)
.where("id = ?")
# Q 34 : # InventoryUnit.accessible_by(current_ability, :show).find(params[:id])
Query(InventoryUnit)
.where("id = ?")
# Q 35 : # OptionType.order(:name)
Query(OptionType)
.order('name')
# Q 36 : # Order.find_by!(number: params[:order_id])
Query(Order)
.where("number = ?")
# Q 37 : # Order.find_by!(number: params[:order_id])
Query(Order)
.where("number = ?")
# Q 38 : # Order.includes(:adjustments).find_by!(number: params[:order_id])
Query(Order)
.includes('adjustments')
.where("number = ?")
# Q 39 : # Order.includes(line_items: [variant: [:option_values, :images, :product]], bill_address: :state, ship_address: :state).find_by!(number: params[:id])
Query(Order)
.where("number = ?")
# Q 40 : # Payment.find_by!(number: params[:id])
Query(Payment)
.where("number = ?")
# Q 41 : # PaymentMethod.available_on_back_end.select
Query(PaymentMethod)

# Q 42 : # PaymentMethod.available_on_front_end.select
Query(PaymentMethod)

# Q 43 : # PaymentMethod.find(params[:id])
Query(PaymentMethod)
.where("id = ?")
# Q 44 : # Product.accessible_by(current_ability, :show).active.includes(*product_includes)
Query(Product)

# Q 45 : # Product.friendly.find(params[:id])
Query(Product)
.where("id = ?")
# Q 46 : # Product.friendly.includes(*variant_edit_includes).find(params[:product_id])
Query(Product)
.where("id = ?")
# Q 47 : # Product.friendly.includes(*variant_index_includes).find(params[:product_id])
Query(Product)
.where("id = ?")
# Q 48 : # Product.with_deleted.accessible_by(current_ability, :show).includes(*product_includes)
Query(Product)

# Q 49 : # Product.with_deleted.friendly.find(params[:id])
Query(Product)
.where("id = ?")
# Q 50 : # Product.with_deleted.friendly.find(params[:product_id])
Query(Product)
.where("id = ?")
# Q 51 : # Promotion.active.find_by(path: path)
Query(Promotion)
.where("path = ?")
# Q 52 : # Prototype.find(params[:id])
Query(Prototype)
.where("id = ?")
# Q 53 : # Prototype.order("name asc")
Query(Prototype)
.order('name')
# Q 54 : # ShippingCategory.order(:name)
Query(ShippingCategory)
.order('name')
# Q 55 : # Spree.user_class.accessible_by(current_ability, :show).find(params[:id])
# Q 56 : # Spree.user_class.accessible_by(current_ability, :show).find(params[:user_id])
# Q 57 : # Spree.user_class.find(order_params[:user_id])
# Q 58 : # Spree.user_class.find_by(email: DEFAULT_CREATED_BY_EMAIL)
# Q 59 : # Spree.user_class.find_by(email: order_params[:email])
# Q 60 : # Spree.user_class.find_by(id: doorkeeper_token.resource_owner_id)
# Q 61 : # Spree.user_class.find_by(id: order_params[:user_id])
# Q 62 : # Spree.user_class.find_by(id: params[:user_id])
# Q 63 : # Spree.user_class.find_by(spree_api_key: api_key.to_s)
# Q 64 : # Spree::Api::Dependencies.storefront_current_order_finder.constantize.new.execute(store: spree_current_store, user: spree_user, token: order_token, currency: current_currency)
# Q 65 : # Spree::Classification.find_by(product_id: params[:product_id], taxon_id: params[:taxon_id])
Query(Classification)
.where("product_id = ?")
.where("taxon_id = ?")
# Q 66 : # Spree::CustomerReturn.accessible_by(current_ability, :show).find(params[:id])
Query(CustomerReturn)
.where("id = ?")
# Q 67 : # Spree::OptionType.accessible_by(current_ability, :destroy).find(params[:id])
Query(OptionType)
.where("id = ?")
# Q 68 : # Spree::OptionType.accessible_by(current_ability, :show).find(params[:id])
Query(OptionType)
.where("id = ?")
# Q 69 : # Spree::OptionType.accessible_by(current_ability, :update).find(params[:id])
Query(OptionType)
.where("id = ?")
# Q 70 : # Spree::OptionType.find(params[:option_type_id]).option_values.accessible_by(current_ability, :show)
Query(OptionValue)
.where("id = ?")
.where("spree/option_type_id = ?")
# Q 71 : # Spree::OptionType.includes(:option_values).accessible_by(current_ability).where(id: params[:ids].split(","))
Query(OptionType)
.includes('option_values')
.where("id = ?")
# Q 72 : # Spree::OptionValue.where(option_type_id: option_type.id, name: opt_value).first_or_initialize
Query(OptionValue)
.where("option_type_id = ?")
.where("name = ?")
# Q 73 : # Spree::Order.includes(:adjustments).find_by!(number: params[:id])
Query(Order)
.includes('adjustments')
.where("number = ?")
# Q 74 : # Spree::Order.includes(:line_items).find_by!(number: order_id)
Query(Order)
.includes('line_items')
.where("number = ?")
# Q 75 : # Spree::Order.preload(:user).accessible_by(current_ability, :index).ransack(params[:q])
Query(Order)
.includes('user')
# Q 76 : # Spree::Payment.find_by(response_code: authorization_code).try(:order)
Query(Payment)
.where("response_code = ?")
.select('order')
# Q 77 : # Spree::Product.accessible_by(current_ability, :show).friendly.find(params[:product_id])
Query(Product)
.where("id = ?")
# Q 78 : # Spree::Product.joins(:taxons).where(spree_taxons: { id: taxons.pluck(:id) }).pluck(:id).uniq
Query(Product)
.where("id = ?")
.select('id')
.distinct('')
# Q 79 : # Spree::ProductProperty.where(property: brand_property).joins(product: :taxons).where("#{
# Spree::Taxon.table_name}.id" => [taxon] + taxon.descendants)
Query(ProductProperty)
.where("property = ?")
.where("id" = ?")
# Q 80 : # Spree::ProductProperty.where(property_id: brand_property.id).pluck(:value).uniq.map(&:to_s)
Query(ProductProperty)
.where("property_id = ?")
.select('value')
.distinct('')
# Q 81 : # Spree::Promotion.active.where(id: Spree::Promotion::Actions::FreeShipping.pluck(:promotion_id), path: nil)
Query(Promotion)
.where("id = ?")
.where("path = ?")
# Q 82 : # Spree::PromotionCategory.order(:name)
Query(PromotionCategory)
.order('name')
# Q 83 : # Spree::Property.accessible_by(current_ability, :show).find(params[:id])
Query(Property)
.where("id = ?")
# Q 84 : # Spree::Property.accessible_by(current_ability, :show).find_by!(name: params[:id])
Query(Property)
.where("name = ?")
# Q 85 : # Spree::Property.pluck(:name)
Query(Property)
.select('name')
# Q 86 : # Spree::ReturnItem.accessible_by(current_ability).where(inventory_unit_id: @order.inventory_units.pluck(:id)).map(&:customer_return).uniq.compact
Query(ReturnItem)
.where("inventory_unit_id = ?")
.distinct('')
.where("id != 0")
# Q 87 : # Spree::ReturnItem.where(inventory_unit: @return_item.inventory_unit).where.not(reimbursement_id: nil).any?
Query(ReturnItem)
.where("inventory_unit = ?")
.where("reimbursement_id = ?")
# Q 88 : # Spree::ReturnItem.where(inventory_unit_id: inventory_unit_id).where.not(id: id).not_cancelled.each(&:cancel!)
Query(ReturnItem)
.where("inventory_unit_id = ?")
.where("id = ?")
# Q 89 : # Spree::ReturnItem.where(inventory_unit_id: inventory_unit_id, reception_status: COMPLETED_RECEPTION_STATUSES).first
Query(ReturnItem)
.where("inventory_unit_id = ?")
.where("reception_status = ?")
.return_limit('1')
# Q 90 : # Spree::Shipment.accessible_by(current_ability, :update).readonly(false).find_by!(number: params[:id])
Query(Shipment)
.where("number = ?")
# Q 91 : # Spree::Shipment.accessible_by(current_ability, :update).readonly(false).find_by!(number: params[:id])
Query(Shipment)
.where("number = ?")
# Q 92 : # Spree::Shipment.reverse_chronological.joins(:order).where(spree_orders: { user_id: current_api_user.id }).includes(mine_includes).ransack(params[:q]).result.page(params[:page]).per(params[:per_page])
Query(Shipment)
.joins('order')
.where("user_id = ?")
# Q 93 : # Spree::StockItem.find_by(variant_id: inventory_unit.variant_id, stock_location_id: customer_return.stock_location_id)
Query(StockItem)
.where("variant_id = ?")
.where("stock_location_id = ?")
# Q 94 : # Spree::StockItem.where(stock_location_id: shipment.stock_location_id, variant_id: variant_id).first
Query(StockItem)
.where("stock_location_id = ?")
.where("variant_id = ?")
.return_limit('1')
# Q 95 : # Spree::StockLocation.active.joins(:stock_items).where(spree_stock_items: { variant_id: requested_variant_ids }).distinct
Query(StockLocation)
.joins('stock_items')
.where("variant_id = ?")
.distinct('')
# Q 96 : # Spree::StoreCreditCategory.order(:name)
Query(StoreCreditCategory)
.order('name')
# Q 97 : # Spree::TaxCategory.order(:name)
Query(TaxCategory)
.order('name')
# Q 98 : # Spree::Taxon.includes(:children).accessible_by(current_ability).order(:taxonomy_id, :lft)
Query(Taxon)
.order('taxonomy_id, lft')
# Q 99 : # Spree::Taxonomy.accessible_by(current_ability, :show).find(params[:taxonomy_id])
Query(Taxonomy)
.where("id = ?")
# Q 100 : # Spree::Variant.where(product_id: variant.product_id, is_master: variant.is_master?).in_stock_or_backorderable
Query(Variant)
.where("product_id = ?")
.where("is_master = ?")
# Q 101 : # Spree::Zone.accessible_by(current_ability, :show).find(params[:id])
Query(Zone)
.where("id = ?")
# Q 102 : # State.accessible_by(current_ability).order("name ASC")
Query(State)
.order('name')
# Q 103 : # State.order(:name)
Query(State)
.order('name')
# Q 104 : # StockItem.accessible_by(current_ability, :destroy).find(params[:id])
Query(StockItem)
.where("id = ?")
# Q 105 : # StockItem.accessible_by(current_ability, :update).find(params[:id])
Query(StockItem)
.where("id = ?")
# Q 106 : # StockItem.find(params[:id])
Query(StockItem)
.where("id = ?")
# Q 107 : # StockLocation.accessible_by(current_ability, :show).find(params[:id])
Query(StockLocation)
.where("id = ?")
# Q 108 : # StockLocation.accessible_by(current_ability, :show).find(params[:stock_location_id])
Query(StockLocation)
.where("id = ?")
# Q 109 : # StockLocation.accessible_by(current_ability, :show).find(params[:stock_location_id])
Query(StockLocation)
.where("id = ?")
# Q 110 : # StockLocation.find(params[:stock_location_id])
Query(StockLocation)
.where("id = ?")
# Q 111 : # StockLocation.find(params[:stock_location_id])
Query(StockLocation)
.where("id = ?")
# Q 112 : # StockLocation.find(params[:transfer_destination_location_id])
Query(StockLocation)
.where("id = ?")
# Q 113 : # StockLocation.find(params[:transfer_source_location_id])
Query(StockLocation)
.where("id = ?")
# Q 114 : # StockTransfer.find_by!(number: params[:id])
Query(StockTransfer)
.where("number = ?")
# Q 115 : # Store.by_url(domain).first
Query(Store)
.return_limit('1')
# Q 116 : # Store.find(params[:id])
Query(Store)
.where("id = ?")
# Q 117 : # StoreCreditEvent.find_by(authorization_code: auth_code, action: Spree::StoreCredit::CAPTURE_ACTION)
Query(StoreCreditEvent)
.where("authorization_code = ?")
.where("action = ?")
# Q 118 : # TaxCategory.find_by(is_default: true)
Query(TaxCategory)
.where("is_default = ?")
# Q 119 : # TaxCategory.order(:name)
Query(TaxCategory)
.order('name')
# Q 120 : # TaxCategory.order(:name)
Query(TaxCategory)
.order('name')
# Q 121 : # TaxCategory.order(:name)
Query(TaxCategory)
.order('name')
# Q 122 : # Taxon.find(parent_id.to_i)
Query(Taxon)
.where("id = ?")
# Q 123 : # Taxon.find(taxon_id)
Query(Taxon)
.where("id = ?")
# Q 124 : # Taxon.friendly.find(params[:id])
Query(Taxon)
.where("id = ?")
# Q 125 : # Taxon.order(:name)
Query(Taxon)
.order('name')
# Q 126 : # Taxonomy.accessible_by(current_ability, :show).find(params[:id])
Query(Taxonomy)
.where("id = ?")
# Q 127 : # Taxonomy.find(params[:taxonomy_id])
Query(Taxonomy)
.where("id = ?")
# Q 128 : # Variant.find(params[:id])
Query(Variant)
.where("id = ?")
# Q 129 : # Variant.find(params[:variant_id])
Query(Variant)
.where("id = ?")
# Q 130 : # Variant.only_deleted.where(product_id: parent.id)
Query(Variant)
.where("product_id = ?")
# Q 131 : # Zone.order(:name)
Query(Zone)
.order('name')
# Q 132 : # Zone.order(:name)
Query(Zone)
.order('name')
# Q 133 : # Zone.order(:name)
Query(Zone)
.order('name')
# Q 134 : # active.where(display_on: [:back_end, :both])
Query(PaymentMethod)
.where("display_on = ?")
# Q 135 : # active.where(display_on: [:front_end, :back_end, :both])
Query(PaymentMethod)
.where("display_on = ?")
# Q 136 : # active.where(display_on: [:front_end, :both])
Query(PaymentMethod)
.where("display_on = ?")
# Q 137 : # adjustments.competing_promos.eligible.reorder("amount ASC, created_at DESC, id DESC").first
Query(Adjustment)
.order('amount, created_at')
.return_limit('1')
# Q 138 : # adjustments.where(order: order).pluck(:adjustable_id)
Query(Adjustment)
.where("order = ?")
.select('adjustable_id')
# Q 139 : # all.select
# Q 140 : # all_adjustments.eligible.nonzero.promotion.map { |a|
#   
#   a.source.promotion_id
# }.uniq
# Q 141 : # args.first
# Q 142 : # array.select
# Q 143 : # attributes.select
# Q 144 : # attributes[:payments_attributes].first
# Q 145 : # attributes[:payments_attributes].first
# Q 146 : # attributes[:payments_attributes].first
# Q 147 : # attributes[:payments_attributes].first
# Q 148 : # backordered_inventory_units.first(number)
# Q 149 : # backordered_per_variant(stock_item).select
Query(InventoryUnit)

# Q 150 : # case kind
# when "country"
#   
#   zoneables when "state"
#   
#   zoneables.collect(&:country)
# else
#   
#   []
# end.flatten.compact.uniq
# Q 151 : # child.active_products.distinct.select("spree_products.*, spree_products_taxons.position").where(products_arel[:id].not_in(products.map(&:id))).limit(to_get)
# Q 152 : # classifications.where(taxon: taxon)
Query(Classification)
.where("taxon = ?")
# Q 153 : # collection.where(stock_location: stock_location)
# Q 154 : # collection_finder.new(scope: scope, params: params).execute
# Q 155 : # collection_finder.new(scope: scope, params: params, current_currency: current_currency).execute
# Q 156 : # collection_finder.new(user: spree_user).execute
# Q 157 : # completed_orders.first
# Q 158 : # contents.map { |item|
#   
#   item.inventory_unit.variant_id
# }.compact.uniq
# Q 159 : # contents.select
# Q 160 : # contents.select(&:backordered?)
# Q 161 : # contents.select(&:on_hand?)
# Q 162 : # credit_cards.default.first
Query(CreditCard)
.return_limit('1')
# Q 163 : # current_api_user.orders.incomplete.order(:created_at).last
# Q 164 : # customer_return.order
Query(CustomerReturn)
.order('')
# Q 165 : # eager_load(:exchange_inventory_units).where(spree_inventory_units: { original_return_item_id: nil }).distinct
Query(ReturnItem)
.includes('exchange_inventory_units')
.where("original_return_item_id = ?")
.distinct('')
# Q 166 : # exchange_inventory_units.map(&:shipment).uniq
# Q 167 : # find("#preferences_#{
# preference}")
# Q 168 : # find(".select2-container")
# Q 169 : # find(*args)
Query(PaymentMethod)
.where("id = ?")
# Q 170 : # find(:css, options[:from])
# Q 171 : # find(:label, from, class: "!select2-offscreen")
# Q 172 : # find_by(default_tax: true)
Query(Zone)
.where("default_tax = ?")
# Q 173 : # find_by(id: country_id)
Query(Country)
.where("id = ?")
# Q 174 : # find_by(iso: "US")
Query(Country)
.where("iso = ?")
# Q 175 : # find_by(name: "GlobalZone")
# Q 176 : # find_by(name: RETURN_PROCESSING_REASON, mutable: false)
Query(RefundReason)
.where("name = ?")
.where("mutable = ?")
# Q 177 : # ids_or_records_or_names.flatten.map do |t|
#   
#   case t
#   when Integer
#     
#     Taxon.find_by(id: t) when ApplicationRecord
#     
#     t when String
#     
#     Taxon.find_by(name: t) || Taxon.where("#{
#     taxons}.permalink LIKE ? OR #{
#     taxons}.permalink = ?", "%/#{
#     t}/", "#{
#     t}/").first
#   end
#   
# end.compact.flatten.uniq
# Q 178 : # includes(:credit_type).order("spree_store_credit_types.priority ASC")
Query(StoreCredit)
.order('priority')
# Q 179 : # includes(:shipment, :order).where.not(spree_shipments: { state: "canceled" }).where(variant_id: stock_item.variant_id).where.not(spree_orders: { completed_at: nil }).backordered.order("spree_orders.completed_at ASC")
Query(InventoryUnit)
.includes('shipment')
.includes('order')
.where("state = ?")
.where("variant_id = ?")
.where("completed_at = ?")
# Q 180 : # incomplete_orders.includes(:adjustments).lock(options[:lock]).find_by(token_order_params)
# Q 181 : # incomplete_orders.lock(options[:lock]).find_by(token_order_params)
# Q 182 : # inventory_units.includes(:line_item).map(&:line_item).uniq
Query(InventoryUnit)
.includes('line_item')
.distinct('')
# Q 183 : # inventory_units.map(&:variant_id).uniq
Query(InventoryUnit)
.distinct('')
# Q 184 : # inventory_units.where(line_item_id: line_item.id, variant_id: line_item.variant_id || variant.id)
Query(InventoryUnit)
.where("line_item_id = ?")
.where("variant_id = ?")
# Q 185 : # inventory_units.where(variant_id: variant.id)
Query(InventoryUnit)
.where("variant_id = ?")
# Q 186 : # items.select
# Q 187 : # joins("        INNER JOIN spree_order_promotions
#         ON spree_order_promotions.promotion_id = #{
# table_name}.id
# ").distinct
Query(Promotion)
.distinct('')
# Q 188 : # joins(:classifications).where(Classification.table_name => { taxon_id: ids })
# Q 189 : # joins(:order).merge(Spree::Order.complete)
Query(Adjustment)
.joins('order')
# Q 190 : # joins(:order).merge(Spree::Order.incomplete)
Query(Adjustment)
.joins('order')
# Q 191 : # joins(:prices).where("spree_prices.currency = ?", currency).where("spree_prices.amount IS NOT NULL").distinct
Query(Variant)
.joins('prices')
.distinct('')
# Q 192 : # joins(:stock_items).where("count_on_hand > ? OR track_inventory = ?", 0, false)
Query(Variant)
.joins('stock_items')
# Q 193 : # joins(:stock_items).where(spree_stock_items: { backorderable: true })
Query(Variant)
.joins('stock_items')
.where("backorderable = ?")
# Q 194 : # joins(:zone_members).where("(spree_zone_members.zoneable_type = 'Spree::State' AND
#             spree_zone_members.zoneable_id IN (?))
#            OR (spree_zone_members.zoneable_type = 'Spree::Country' AND
#             spree_zone_members.zoneable_id IN (?))", zone.state_ids, zone.states.pluck(:country_id)).distinct
Query(Zone)
.joins('zone_members')
.distinct('')
# Q 195 : # joins(countries: :zones).where("zone_members_spree_countries_join.zone_id = ?", zone.id).distinct
Query(Zone)
.distinct('')
# Q 196 : # label.first(:xpath, ".//..")
# Q 197 : # line_item.variant.prices.where(currency: currency).first
Query(Price)
.where("id = ?")
.where("spree/variant_id = ?")
.where("currency = ?")
.return_limit('1')
# Q 198 : # line_items.select(&:insufficient_stock?)
Query(LineItem)
.select('insufficient_stock?')
# Q 199 : # matches.first
# Q 200 : # members.pluck(:zoneable_id)
# Q 201 : # members.pluck(:zoneable_id)
# Q 202 : # model_class.find(params[:id])
# Q 203 : # model_class.where(nil)
# Q 204 : # not_cancelled.find_by(inventory_unit: inventory_unit)
# Q 205 : # not_discontinued.joins(master: :prices).where("#{
# Product.quoted_table_name}.available_on <= ?", available_on)
# Q 206 : # not_nil_scope.order("created_at ASC").pluck(:zoneable_type).last
# Q 207 : # options.first
# Q 208 : # order(:name)
Query(Property)
.order('name')
# Q 209 : # order("coalesce(spree_shipments.shipped_at, spree_shipments.created_at) desc", id: :desc)
Query(Shipment)

# Q 210 : # order("spree_orders.completed_at IS NULL", completed_at: :desc, created_at: :desc)
Query(Order)
.order('completed_at, created_at')
# Q 211 : # order(created_at: :desc)
Query(StockMovement)
.order('created_at')
# Q 212 : # order(created_at: :desc)
Query(StoreCreditEvent)
.order('created_at')
# Q 213 : # order(default: :desc, name: :asc)
Query(StockLocation)
.order('default, name')
# Q 214 : # order.payments.where(source_type: payment_source_class.to_s, payment_method_id: id).pluck(:source_id).uniq
Query(Payment)
.where("order_id = ?")
.where("source_type = ?")
.where("payment_method_id = ?")
.select('source_id')
.distinct('')
# Q 215 : # order.promotions.pluck(:id)
Query(Promotion)
.where("order_id = ?")
.select('id')
# Q 216 : # order.return_authorizations.accessible_by(current_ability, :destroy).find(params[:id])
Query(ReturnAuthorization)
.where("order_id = ?")
.where("id = ?")
# Q 217 : # order.return_authorizations.accessible_by(current_ability, :show).find(params[:id])
Query(ReturnAuthorization)
.where("order_id = ?")
.where("id = ?")
# Q 218 : # order.return_authorizations.accessible_by(current_ability, :update).find(params[:id])
Query(ReturnAuthorization)
.where("order_id = ?")
.where("id = ?")
# Q 219 : # order.return_authorizations.accessible_by(current_ability, :update).find(params[:id])
Query(ReturnAuthorization)
.where("order_id = ?")
.where("id = ?")
# Q 220 : # order_promotions.where(promotion_id: valid_promotion_ids).uniq(&:promotion_id)
Query(OrderPromotion)
.where("promotion_id = ?")
.distinct('')
# Q 221 : # order_taxons(order).where(id: taxons_including_children_ids)
Query(Taxon)
.where("id = ?")
# Q 222 : # orders.where(store: store).incomplete.includes(line_items: [variant: [:images, :option_values, :product]]).order("created_at DESC").first
Query(Order)
.where("store = ?")
.order('created_at')
.return_limit('1')
# Q 223 : # parent.all_adjustments.find(params[:id])
# Q 224 : # parent.send(controller_name).find(params[:id])
# Q 225 : # payment_methods.find(payment_method_id)
Query(PaymentMethod)
.where("id = ?")
# Q 226 : # payment_source.actions.select
# Q 227 : # payments.from_credit_card.pluck(:source_id).uniq
Query(Payment)
.select('source_id')
.distinct('')
# Q 228 : # payments.from_credit_card.valid.pluck(:source_id).uniq
Query(Payment)
.select('source_id')
.distinct('')
# Q 229 : # payments.select(&:checkout?)
Query(Payment)
.select('checkout?')
# Q 230 : # payments.select(&:pending?)
Query(Payment)
.select('pending?')
# Q 231 : # pluck(:state).uniq
Query(Order)
.select('state')
.distinct('')
# Q 232 : # product_scope.find_by(id: id)
# Q 233 : # product_scope.friendly.distinct(false).find(id.to_s)
# Q 234 : # product_scope.where(id: params[:ids].split(",").flatten)
# Q 235 : # product_variants.select
# Q 236 : # promotion.actions.pluck(:id)
Query(Promotion)
.select('id')
# Q 237 : # promotion.actions.where(type: "Spree::Promotion::Actions::CreateLineItems").pluck(:id)
Query(Promotion)
.where("type = ?")
.select('id')
# Q 238 : # promotions.pluck(:code).compact.first
Query(Promotion)
.select('code')
.where("id != 0")
.return_limit('1')
# Q 239 : # rates.select
# Q 240 : # rates.select(&:included_in_price)
# Q 241 : # record.class.columns_hash[@field].limit
# Q 242 : # resource_finder.new(number: params[:number], token: order_token).execute.take
# Q 243 : # resource_finder.new(user: spree_user, number: params[:id]).execute.take
# Q 244 : # resource_finder.new.execute(scope: scope, params: params)
# Q 245 : # results.select(&:error)
# Q 246 : # return_items.find
Query(ReturnItem)
.where("id = ?")
# Q 247 : # return_items.first.inventory_unit.order
Query(Order)
.return_limit('1')
.where("id = ?")
.where("id = ?")
# Q 248 : # return_items.not_cancelled.first
Query(ReturnItem)
.return_limit('1')
# Q 249 : # return_items.select(&:exchange_required?)
Query(ReturnItem)
.select('exchange_required?')
# Q 250 : # return_items.select(&:exchange_required?)
Query(ReturnItem)
.select('exchange_required?')
# Q 251 : # return_items.select(&:return_authorization_id)
Query(ReturnItem)
.select('return_authorization_id')
# Q 252 : # returned_items.select(&:accepted?)
# Q 253 : # returned_items.select(&:manual_intervention_required?)
# Q 254 : # returned_items.select(&:pending?)
# Q 255 : # returned_items.select(&:rejected?)
# Q 256 : # rule_eligibility.detect { |_, eligibility|
#   
#   eligibility
# }.first
# Q 257 : # rules.select
# Q 258 : # rules.where(type: "Spree::Promotion::Rules::Product").map(&:products).flatten.uniq
# Q 259 : # scope.accessible_by(current_ability, :destroy).find(params[:id])
# Q 260 : # scope.accessible_by(current_ability, :destroy).find(params[:id])
# Q 261 : # scope.accessible_by(current_ability, :update).find(params[:id])
# Q 262 : # scope.accessible_by(current_ability, :update).find(params[:id])
# Q 263 : # scope.find(params[:id])
# Q 264 : # scope.find(params[:id])
# Q 265 : # scope.find(params[:id])
# Q 266 : # scope.find(params[:id])
# Q 267 : # scope.find(params[:id])
# Q 268 : # scope.find(params[:id])
# Q 269 : # scope.find_by(id: params[:iso].upcase)
# Q 270 : # scope.find_by(iso3: params[:iso].upcase)
# Q 271 : # scope.find_by(iso: params[:iso].upcase)
# Q 272 : # scope.find_by(permalink: params[:id])
# Q 273 : # scope.find_by(slug: params[:id])
# Q 274 : # scope.images.accessible_by(current_ability, :destroy).find(params[:id])
# Q 275 : # scope.images.accessible_by(current_ability, :update).find(params[:id])
# Q 276 : # scope.includes(*variant_includes).find(params[:id])
# Q 277 : # scope.pluck(:value).uniq
# Q 278 : # scope.preload(:tax_category)
# Q 279 : # scope.preload(master: :images)
# Q 280 : # scope.preload(master: :prices)
# Q 281 : # scope.ransack(params[:q]).result.distinct
# Q 282 : # scope.ransack(params[:q]).result.includes(:country)
# Q 283 : # scope.where(attribute.eq(value))
# Q 284 : # scope.where(attribute.gt(value))
# Q 285 : # scope.where(attribute.gteq(value))
# Q 286 : # scope.where(attribute.lt(value))
# Q 287 : # scope.where(attribute.lteq(value))
# Q 288 : # scope.where(attribute.matches("%#{
# value}%"))
# Q 289 : # scope.where(id: params[:ids])
# Q 290 : # self.checkout_steps.keys.last
# Q 291 : # self.class.where(is_default: true).where.not(id: id).first
# Q 292 : # shipment_states.first
# Q 293 : # spree_current_order.line_items.find(params[:line_item_id])
# Q 294 : # stock_items.where(variant_id: variant_id).order(:id).first
Query(StockItem)
.where("variant_id = ?")
.order('')
.return_limit('1')
# Q 295 : # stock_movement.originator.order
Query(Originator)
.where("id = ?")
# Q 296 : # stock_movements.joins(:stock_item).where("spree_stock_items.stock_location_id" => location_id)
Query(StockMovement)
.joins('stock_item')
.where("stock_location_id" = ?")
# Q 297 : # store_credit.store_credit_events.where(amount: amount_in_cents / 100.0.to_d, action: Spree::StoreCredit::ELIGIBLE_ACTION)
Query(StoreCredit)
.where("amount = ?")
.where("action = ?")
# Q 298 : # store_credit_events.find_by(action: AUTHORIZE_ACTION, authorization_code: authorization_code)
Query(StoreCreditEvent)
.where("action = ?")
.where("authorization_code = ?")
# Q 299 : # store_credit_events.find_by(action: AUTHORIZE_ACTION, authorization_code: authorization_code)
Query(StoreCreditEvent)
.where("action = ?")
.where("authorization_code = ?")
# Q 300 : # store_credit_events.find_by(action: CAPTURE_ACTION, authorization_code: authorization_code)
Query(StoreCreditEvent)
.where("action = ?")
.where("authorization_code = ?")
# Q 301 : # super.includes(:default_price, option_values: :option_type)
# Q 302 : # super.order(:name)
# Q 303 : # super.order(:name)
# Q 304 : # super.order(position: :asc)
# Q 305 : # taxon_and_ancestors.map(&:taxonomy_id).flatten.uniq
# Q 306 : # taxonomy.taxons.accessible_by(current_ability, :show).find(params[:id])
Query(Taxon)
.where("taxonomy_id = ?")
.where("id = ?")
# Q 307 : # taxons.joins(:taxonomy).find_by(spree_taxonomies: { name: Spree.t(:taxonomy_brands_name) })
Query(Taxon)
.where("name = ?")
# Q 308 : # taxons.joins(:taxonomy).find_by(spree_taxonomies: { name: Spree.t(:taxonomy_categories_name) })
Query(Taxon)
.where("name = ?")
# Q 309 : # taxons.map(&:self_and_ancestors).flatten.uniq
Query(Taxon)
.distinct('')
# Q 310 : # variants_including_master.with_deleted.find_by(is_master: true)
# Q 311 : # where("#{
# Product.quoted_table_name}.discontinue_on IS NULL or #{
# Product.quoted_table_name}.discontinue_on >= ?", Time.zone.now)
# Q 312 : # where("#{
# Spree::Variant.quoted_table_name}.deleted_at IS NULL")
Query(Variant)

# Q 313 : # where("quoted.amount != 0")
Query(Adjustment)

# Q 314 : # where("quoted.amount < 0")
Query(Adjustment)

# Q 315 : # where("quoted.amount >= 0")
Query(Adjustment)

# Q 316 : # where("avs_response IN (?) OR (cvv_response_code IS NOT NULL and cvv_response_code != 'M') OR state = 'failed'", RISKY_AVS_CODES)
Query(Payment)

# Q 317 : # where("lower(#{
# table_name}.code) = ?", coupon_code.strip.downcase).includes(:promotion_actions).where.not(spree_promotion_actions: { id: nil }).first
Query(Promotion)
.includes('promotion_actions')
.where("id = ?")
.return_limit('1')
# Q 318 : # where("name = ? OR abbr = ?", name_or_abbr, name_or_abbr)
Query(State)

# Q 319 : # where("source_type = 'Spree::Payment' AND amount < 0 AND state = 'completed'")
Query(Payment)

# Q 320 : # where("spree_promotions.starts_at IS NULL OR spree_promotions.starts_at < ?", Time.current).where("spree_promotions.expires_at IS NULL OR spree_promotions.expires_at > ?", Time.current)
Query(Promotion)

# Q 321 : # where("tracking IS NOT NULL AND tracking != ''")
Query(Shipment)

# Q 322 : # where("url like ?", "%#{
# url}%")
Query(Store)

# Q 323 : # where("zoneable_id IS NULL OR zoneable_type != ?", "Spree::#{
# kind.classify}")
Query(ZoneMember)

# Q 324 : # where(acceptance_status: "accepted")
Query(ReturnItem)
.where("acceptance_status = ?")
# Q 325 : # where(acceptance_status: "manual_intervention_required")
Query(ReturnItem)
.where("acceptance_status = ?")
# Q 326 : # where(acceptance_status: "pending")
Query(ReturnItem)
.where("acceptance_status = ?")
# Q 327 : # where(acceptance_status: "rejected")
Query(ReturnItem)
.where("acceptance_status = ?")
# Q 328 : # where(acceptance_status: %w{pending manual_intervention_required})
Query(ReturnItem)
.where("acceptance_status = ?")
# Q 329 : # where(active: true)
Query(StockLocation)
.where("active = ?")
# Q 330 : # where(active: true)
# Q 331 : # where(active: true).order(position: :asc)
Query(PaymentMethod)
.where("active = ?")
.order('position')
# Q 332 : # where(adjustable_type: "Spree::LineItem")
Query(Adjustment)
.where("adjustable_type = ?")
# Q 333 : # where(adjustable_type: "Spree::Shipment")
Query(Adjustment)
.where("adjustable_type = ?")
# Q 334 : # where(advertise: true)
Query(Promotion)
.where("advertise = ?")
# Q 335 : # where(completed_at: nil)
Query(Order)
.where("completed_at = ?")
# Q 336 : # where(completed_at: start_date..end_date)
Query(Order)
.where("completed_at = ?")
# Q 337 : # where(created_at: start_date..end_date)
Query(Order)
.where("created_at = ?")
# Q 338 : # where(default: true)
Query(CreditCard)
.where("default = ?")
# Q 339 : # where(default_tax: true)
Query(Zone)
.where("default_tax = ?")
# Q 340 : # where(eligible: true)
Query(Adjustment)
.where("eligible = ?")
# Q 341 : # where(included: false)
Query(Adjustment)
.where("included = ?")
# Q 342 : # where(included: true)
Query(Adjustment)
.where("included = ?")
# Q 343 : # where(included_in_price: true)
Query(TaxRate)
.where("included_in_price = ?")
# Q 344 : # where(is_master: false).or(where("            #{
# Variant.quoted_table_name}.id IN (
#               SELECT MIN(#{
# Variant.quoted_table_name}.id) FROM #{
# Variant.quoted_table_name}
#               GROUP BY #{
# Variant.quoted_table_name}.product_id
#               HAVING COUNT(*) = 1
#             )
# "))
Query(Variant)
.where("is_master = ?")
# Q 345 : # where(mandatory: false)
Query(Adjustment)
.where("mandatory = ?")
# Q 346 : # where(reception_status: "awaiting")
Query(ReturnItem)
.where("reception_status = ?")
# Q 347 : # where(reception_status: "received")
Query(ReturnItem)
.where("reception_status = ?")
# Q 348 : # where(reimbursement_id: nil)
Query(ReturnItem)
.where("reimbursement_id = ?")
# Q 349 : # where(reimbursement_id: nil)
Query(Refund)
.where("reimbursement_id = ?")
# Q 350 : # where(reimbursement_status: "reimbursed")
Query(IncompleteReimbursementError)
.where("reimbursement_status = ?")
# Q 351 : # where(source_type: "Spree::CreditCard")
Query(Payment)
.where("source_type = ?")
# Q 352 : # where(source_type: "Spree::PromotionAction")
Query(Adjustment)
.where("source_type = ?")
# Q 353 : # where(source_type: "Spree::ReturnAuthorization")
Query(Adjustment)
.where("source_type = ?")
# Q 354 : # where(source_type: "Spree::TaxRate")
Query(Adjustment)
.where("source_type = ?")
# Q 355 : # where(source_type: Spree::StoreCredit.to_s)
Query(Payment)
.where("source_type = ?")
# Q 356 : # where(source_type: competing_promos_source_types)
Query(Adjustment)
.where("source_type = ?")
# Q 357 : # where(state: "closed")
Query(Adjustment)
.where("state = ?")
# Q 358 : # where(state: "open")
Query(Adjustment)
.where("state = ?")
# Q 359 : # where(state: s)
Query(Shipment)
.where("state = ?")
# Q 360 : # where(state: s.to_s)
Query(Payment)
.where("state = ?")
# Q 361 : # where(tax_category_id: category.try(:id))
Query(TaxRate)
.where("tax_category_id = ?")
# Q 362 : # where(type: t)
Query(PromotionRule)
.where("type = ?")
# Q 363 : # where(type: t)
Query(PromotionAction)
.where("type = ?")
# Q 364 : # where(zone_id: Spree::Zone.potential_matching_zones(zone).pluck(:id))
Query(TaxRate)
.where("zone_id = ?")
# Q 365 : # where(zone_id: zone.id)
Query(TaxRate)
.where("zone_id = ?")
# Q 366 : # where.not(acceptance_status: %w{pending manual_intervention_required})
Query(ReturnItem)
.where("acceptance_status = ?")
# Q 367 : # where.not(action: [Spree::StoreCredit::ELIGIBLE_ACTION, Spree::StoreCredit::AUTHORIZE_ACTION])
Query(StoreCreditEvent)
.where("action = ?")
# Q 368 : # where.not(code: nil)
Query(Promotion)
.where("code = ?")
# Q 369 : # where.not(completed_at: nil)
Query(Order)
.where("completed_at = ?")
# Q 370 : # where.not(exchange_variant: nil)
Query(ReturnItem)
.where("exchange_variant = ?")
# Q 371 : # where.not(gateway_customer_profile_id: nil)
Query(CreditCard)
.where("gateway_customer_profile_id = ?")
# Q 372 : # where.not(reception_status: "cancelled")
Query(ReturnItem)
.where("reception_status = ?")
# Q 373 : # where.not(reimbursement_id: nil)
Query(ReturnItem)
.where("reimbursement_id = ?")
# Q 374 : # where.not(state: INVALID_STATES)
Query(Payment)
.where("state = ?")
