# Q 3 : # @account.media_attachments.attached.reorder(nil).select(:status_id).distinct
Query(Account)
.joins('media_attachments')
.select('media_attachments.status_id')
.distinct('')
# Q 4 : # @account.statuses.find(params[:id])
Query(Account)
.where("id = ?")
# Q 5 : # @account.statuses.find(params[:status_id])
Query(Account)
.where("id = ?")
# Q 6 : # @account.statuses.joins(:media_attachments).merge(@account.media_attachments).permitted_for(@account, current_account).paginate_by_max_id(limit_param(DEFAULT_STATUSES_LIMIT), params[:max_id], params[:since_id]).reorder(id: :desc).distinct(:id).pluck(:id)
Query(Account)
.order('id')
.distinct('')
.select('id')
# Q 7 : # @account.statuses.where(id: params[:id])
Query(Account)
.where("id = ?")
# Q 11 : # @list.accounts.includes(:account_stat).all
Query(Account)
.joins('list_accounts')
.where("list_accounts.list_id = ?")
# Q 12 : # @list.accounts.includes(:account_stat).paginate_by_max_id(limit_param(DEFAULT_ACCOUNTS_LIMIT), params[:max_id], params[:since_id])
Query(Account)
.joins('list_accounts')
.where("list_accounts.list_id = ?")
# Q 13 : # @status.mentions.find_by(account_id: @options[:delivered_to_account_id])
Query(Mention)
.where("status_id = ?")
.where("account_id = ?")
# Q 14 : # @status.reblogs.includes(:account).references(:account).merge(Account.local).pluck(:account_id)
Query(Status)
.includes('account')
.select('account_id')
# Q 15 : # @status.thread.mentions.where(account: @account).exists?
Query(Mention)
.where("id = ?")
.where("status_id = ?")
.where("account = ?")
.return_limit('1')
# Q 16 : # @status.update(visibility: :limited)
Query(Status)

# Q 17 : # @statuses.preload(:media_attachments, :mentions).page(params[:page]).per(PER_PAGE)
Query(Status)
.includes('media_attachments')
.includes('mentions')
# Q 18 : # @tag.statuses.with_public_visibility.excluding_silenced_accounts.where(Status.arel_table[:id].gteq(Mastodon::Snowflake.id_at(Time.now.utc.beginning_of_day))).joins(:account).group("accounts.domain").reorder("statuses_count desc").pluck("accounts.domain, count(*) AS statuses_count")
Query(Status)
.where("id = ?")
.joins('account')
.group('account.domain, id')
.order('id')
.select('account.domain')
# Q 19 : # Account.by_domain_accounts.find_by(domain: params[:id])
Query(Account)
.where("domain = ?")
# Q 20 : # Account.find(-99)
Query(Account)
.where("id = ?")
# Q 21 : # Account.find(-99)
Query(Account)
.where("id = ?")
# Q 22 : # Account.find(@options[:delivered_to_account_id])
Query(Account)
.where("id = ?")
# Q 23 : # Account.find(account_ids)
Query(Account)
.where("id = ?")
# Q 24 : # Account.find(params[:account_id])
Query(Account)
.where("id = ?")
# Q 25 : # Account.find(params[:account_id])
Query(Account)
.where("id = ?")
# Q 26 : # Account.find(params[:account_id])
Query(Account)
.where("id = ?")
# Q 27 : # Account.find(params[:account_id])
Query(Account)
.where("id = ?")
# Q 28 : # Account.find(params[:account_id])
Query(Account)
.where("id = ?")
# Q 29 : # Account.find(params[:account_id])
Query(Account)
.where("id = ?")
# Q 30 : # Account.find(params[:account_id])
Query(Account)
.where("id = ?")
# Q 31 : # Account.find(params[:account_id])
Query(Account)
.where("id = ?")
# Q 32 : # Account.find(params[:account_id])
Query(Account)
.where("id = ?")
# Q 33 : # Account.find(params[:account_id]).user
Query(Account)
.where("id = ?")
# Q 34 : # Account.find(params[:id])
Query(Account)
.where("id = ?")
# Q 35 : # Account.find(params[:id])
Query(Account)
.where("id = ?")
# Q 36 : # Account.find(params[:id])
Query(Account)
.where("id = ?")
# Q 37 : # Account.find(params[:id])
Query(Account)
.where("id = ?")
# Q 38 : # Account.find(report_params[:account_id])
Query(Account)
.where("id = ?")
# Q 39 : # Account.find_by(id: matches[2])
Query(Account)
.where("id = ?")
# Q 40 : # Account.includes(:active_relationships, :account_stat).references(:active_relationships)
Query(Account)

# Q 41 : # Account.includes(:favourites, :account_stat).references(:favourites).where(favourites: { status_id: @status.id })
Query(Account)
.includes('favourites')
.includes('account_stats')
.where("favourites.status_id = ?")
# Q 42 : # Account.includes(:follow_requests, :account_stat).references(:follow_requests)
Query(Account)

# Q 43 : # Account.includes(:passive_relationships, :account_stat).references(:passive_relationships)
Query(Account)

# Q 44 : # Account.includes(:statuses, :account_stat).references(:statuses)
Query(Account)

# Q 45 : # Account.local.where(username: local_usernames).exists?
Query(Account)
.where("username = ?")
.return_limit('1')
# Q 46 : # Account.local.without_suspended.find_each
Query(Account)

# Q 47 : # Account.recent.includes(:user)
Query(Account)

# Q 48 : # Account.remote.where(domain: domains)
Query(Account)
.where("domain = ?")
# Q 49 : # Account.remote.where.not(domain: DomainAllow.pluck(:domain))
Query(Account)
.where("domain = ?")
# Q 50 : # Account.searchable.where(id: account_ids)
Query(Account)
.where("id = ?")
# Q 51 : # Account.select(:username, :domain, :url).find_remote(username, domain)
Query(Account)
.select('username')
.select('domain')
.select('url')
# Q 52 : # Account.where("id > 0").exists?
Query(Account)
.return_limit('1')
# Q 53 : # Account.where(domain: nil)
Query(Account)
.where("domain = ?")
# Q 54 : # Account.where(domain: params[:by_domain])
Query(Account)
.where("domain = ?")
# Q 55 : # Account.where(domain: value)
Query(Account)
.where("domain = ?")
# Q 56 : # Account.where(id: account_ids)
Query(Account)
.where("id = ?")
# Q 57 : # Account.where(id: account_ids).includes(:account_stat).each_with_object({ })
Query(Account)
.where("id = ?")
# Q 58 : # Account.where(id: account_ids).includes(:account_stat).each_with_object({ })
Query(Account)
.where("id = ?")
# Q 59 : # Account.where(id: account_ids).select("id")
Query(Account)
.where("id = ?")
.select('id')
# Q 60 : # Account.where(id: current_account.following)
Query(Account)
.where("id = ?")
# Q 61 : # Account.where(id: participant_account_ids)
Query(Account)
.where("id = ?")
# Q 62 : # Account.where(id: target_account_ids).select("id, domain").each_with_object({ })
Query(Account)
.where("id = ?")
.select('id, domain')
# Q 64 : # Account.where(uri: json["actor"]).exists?
Query(Account)
.where("uri = ?")
.return_limit('1')
# Q 65 : # AccountConversation.where(account: current_account).find(params[:id])
Query(AccountConversation)
.where("account = ?")
.where("id = ?")
# Q 66 : # AccountConversation.where(account: current_account).paginate_by_id(limit_param(LIMIT), params_slice(:max_id, :since_id, :min_id))
Query(AccountConversation)
.where("account = ?")
# Q 67 : # AccountDomainBlock.where(account_id: receiver_id, domain: statuses.map { |s|
#   
#   s.reblog.account.domain
# }.compact).pluck(:domain).each_with_object({ })
Query(AccountDomainBlock)
.where("account_id = ?")
.where("domain = ?")
.select('domain')
# Q 68 : # AccountIdentityProof.find(proof_id)
Query(AccountIdentityProof)
.where("id = ?")
# Q 69 : # AccountIdentityProof.where(account: current_account).order(provider: :asc, provider_username: :asc)
Query(AccountIdentityProof)
.where("account = ?")
.order('provider, provider_username')
# Q 70 : # AccountModerationNote.find(params[:id])
Query(AccountModerationNote)
.where("id = ?")
# Q 71 : # AccountPin.find_by(account: current_account, target_account: @account)
Query(AccountPin)
.where("account = ?")
# Q 72 : # AccountPin.where(target_account_id: target_account_id, account_id: account_id).delete_all
Query(AccountPin)
.where("account_id = ?")
# Q 73 : # AccountStat.where(last_status_at: nil).or(AccountStat.where(AccountStat.arel_table[:last_status_at].lt(1.month.ago)))
Query(AccountStat)
.where("last_status_at = ?")
# Q 74 : # AccountWarningPreset.find(params[:id])
Query(AccountWarningPreset)
.where("id = ?")
# Q 75 : # AccountWarningPreset.find(warning_preset_id)
Query(AccountWarningPreset)
.where("id = ?")
# Q 81 : # Conversation.find_by(id: OStatus::TagManager.instance.unique_tag_to_local_id(uri, "Conversation"))
Query(Conversation)
.where("id = ?")
# Q 82 : # ConversationMute.select("conversation_id").where(conversation_id: conversation_ids).where(account_id: account_id).each_with_object({ })
Query(ConversationMute)
.select('conversation_id')
.where("conversation_id = ?")
.where("account_id = ?")
# Q 83 : # CustomEmoji.find_by(shortcode: shortcode, domain: @account.domain)
Query(CustomEmoji)
.where("shortcode = ?")
.where("domain = ?")
# Q 84 : # CustomEmoji.listed.includes(:category)
Query(CustomEmoji)
.includes('category')
# Q 85 : # CustomEmoji.local.find(params[:id])
Query(CustomEmoji)
.where("id = ?")
# Q 86 : # CustomEmoji.local.find_by(shortcode: shortcode)
Query(CustomEmoji)
.where("shortcode = ?")
# Q 87 : # CustomEmoji.local.left_joins(:category).reorder("custom_emoji_categories.name ASC NULLS FIRST, custom_emojis.shortcode ASC")
Query(CustomEmoji)
.joins('category')
.order('id, category.name, shortcode')
# Q 88 : # CustomEmoji.where(domain: domains)
Query(CustomEmoji)
.where("domain = ?")
# Q 89 : # CustomEmoji.where(domain: value.strip.downcase)
Query(CustomEmoji)
.where("domain = ?")
# Q 90 : # CustomEmoji.where(id: custom_emoji_ids)
Query(CustomEmoji)
.where("id = ?")
# Q 91 : # CustomEmoji.where(shortcode: shortcodes, domain: domain, disabled: false).each_with_object({ })
Query(CustomEmoji)
.where("shortcode = ?")
.where("domain = ?")
.where("disabled = ?")
# Q 92 : # CustomEmojiCategory.find(category_id)
Query(CustomEmojiCategory)
.where("id = ?")
# Q 93 : # DomainAllow.find(params[:id])
Query(DomainAllow)
.where("id = ?")
# Q 94 : # DomainBlock.find(params[:id])
Query(DomainBlock)
.where("id = ?")
# Q 95 : # DomainBlock.where(domain: domains).destroy_all
Query(DomainBlock)
.where("domain = ?")
# Q 96 : # DomainBlock.with_user_facing_limitations.by_severity
Query(DomainBlock)

# Q 97 : # EmailDomainBlock.find(params[:id])
Query(EmailDomainBlock)
.where("id = ?")
# Q 98 : # Favourite.select("status_id").where(status_id: status_ids).where(account_id: account_id).each_with_object({ })
Query(Favourite)
.select('status_id')
.where("status_id = ?")
.where("account_id = ?")
# Q 99 : # Follow.find_by(account_id: list.account_id, target_account_id: account.id)
Query(Follow)
.where("target_account_id = ?")
# Q 100 : # Follow.find_by(target_account: @account, uri: object_uri)
Query(Follow)
.where("target_account = ?")
.where("uri = ?")
# Q 102 : # Follow.where(account: @account).recent.page(params[:page]).per(FOLLOW_PER_PAGE).preload(:target_account)
Query(Follow)
.includes('target_account')
# Q 104 : # Follow.where(account_id: receiver_id, target_account_id: status.account_id).exists?
Query(Follow)
.where("target_account_id = ?")
.return_limit('1')
# Q 105 : # Follow.where(account_id: receiver_id, target_account_id: statuses.map { |s|
#   
#   s.account_id if s.reblog?
# }.compact, show_reblogs: false).pluck(:target_account_id).each_with_object({ })
Query(Follow)
.where("target_account_id = ?")
.where("show_reblogs = ?")
.select('target_account_id')
# Q 106 : # Follow.where(account_id: receiver_id, target_account_id: statuses.map(&:in_reply_to_account_id).compact).pluck(:target_account_id).each_with_object({ })
Query(Follow)
.where("target_account_id = ?")
.select('target_account_id')
# Q 107 : # Follow.where(target_account: @account).paginate_by_max_id(limit_param(DEFAULT_ACCOUNTS_LIMIT), params[:max_id], params[:since_id])
Query(Follow)
.where("target_account = ?")
# Q 108 : # Follow.where(target_account: @account).recent.page(params[:page]).per(FOLLOW_PER_PAGE).preload(:account)
Query(Follow)
.where("target_account = ?")
# Q 109 : # Follow.where(target_account: Account.where(domain: params[:id])).count
Query(Follow)
.where("target_account = ?")
# Q 110 : # Follow.where(target_account_id: id).count
Query(Follow)
.where("target_account_id = ?")
# Q 111 : # Follow.where(target_account_id: target_account_ids, account_id: account_id).each_with_object({ })
Query(Follow)
.where("target_account_id = ?")
# Q 112 : # FollowRequest.find_by(account: @account, target_account: target_account).destroy
Query(FollowRequest)
.where("target_account = ?")
# Q 113 : # FollowRequest.find_by(account: target_account, target_account: @account)
Query(FollowRequest)
.where("target_account = ?")
# Q 114 : # FollowRequest.find_by(account: target_account, target_account: @account)
Query(FollowRequest)
.where("target_account = ?")
# Q 115 : # FollowRequest.find_by(target_account: @account, uri: object_uri)
Query(FollowRequest)
.where("target_account = ?")
.where("uri = ?")
# Q 116 : # FollowRequest.where(target_account: current_account).paginate_by_max_id(limit_param(DEFAULT_ACCOUNTS_LIMIT), params[:max_id], params[:since_id])
Query(FollowRequest)
.where("target_account = ?")
# Q 117 : # FollowRequest.where(target_account_id: target_account_ids, account_id: account_id).each_with_object({ })
Query(FollowRequest)
.where("target_account_id = ?")
# Q 118 : # Invite.find(params[:id])
Query(Invite)
.where("id = ?")
# Q 119 : # Invite.find_by(code: code)
Query(Invite)
.where("code = ?")
# Q 120 : # Invite.find_by(code: code).nil?
Query(Invite)
.where("code = ?")
# Q 121 : # Invite.find_by(code: invite_code)
Query(Invite)
.where("code = ?")
# Q 122 : # Invite.order(created_at: :desc)
Query(Invite)
.order('created_at')
# Q 123 : # List.where(account: current_account).all
Query(List)
.where("account = ?")
# Q 124 : # List.where(account: current_account).find(params[:id])
Query(List)
.where("account = ?")
.where("id = ?")
# Q 125 : # List.where(account: current_account).find(params[:id])
Query(List)
.where("account = ?")
.where("id = ?")
# Q 126 : # List.where(account: current_account).find(params[:list_id])
Query(List)
.where("account = ?")
.where("id = ?")
# Q 127 : # ListAccount.where(list: @list, account_id: account_ids).destroy_all
Query(ListAccount)
.where("list = ?")
.where("account_id = ?")
# Q 128 : # ListAccount.where(list_id: list.id, account_id: status.in_reply_to_account_id).exists?
Query(ListAccount)
.where("list_id = ?")
.where("account_id = ?")
.return_limit('1')
# Q 129 : # MediaAttachment.attached.find_by!(shortcode: params[:id] || params[:medium_id])
Query(MediaAttachment)
.where("shortcode = ?")
# Q 130 : # MediaAttachment.find_by(shortcode: shortcode).nil?
Query(MediaAttachment)
.where("shortcode = ?")
# Q 131 : # MediaAttachment.joins(:account).merge(Account.by_domain_and_subdomains(options[:domain]))
Query(MediaAttachment)
.joins('account')
# Q 132 : # MediaAttachment.remote.find(params[:id])
Query(MediaAttachment)
.where("id = ?")
# Q 133 : # MediaAttachment.where(account: Account.where(domain: params[:id])).sum(:file_file_size)
Query(MediaAttachment)
.where("account = ?")
# Q 134 : # MediaAttachment.where(account_id: account.id)
Query(MediaAttachment)
.where("account_id = ?")
# Q 135 : # MediaAttachment.where(status_id: options[:status])
Query(MediaAttachment)
.where("status_id = ?")
# Q 136 : # MediaAttachment.where(status_id: status_ids)
Query(MediaAttachment)
.where("status_id = ?")
# Q 137 : # MediaAttachment.where(status_id: status_ids).pluck(:status_id)
Query(MediaAttachment)
.where("status_id = ?")
.select('status_id')
# Q 138 : # Mention.active.where(status_id: statuses.flat_map { |s|
#   
#   [s.id, s.reblog_of_id]
# }.compact).pluck(:status_id, :account_id).each_with_object({ })
Query(Mention)
.where("status_id = ?")
.select('status_id')
# Q 139 : # Mute.eager_load(:target_account).where(account: current_account).paginate_by_max_id(limit_param(DEFAULT_ACCOUNTS_LIMIT), params[:max_id], params[:since_id])
Query(Mute)
.includes('target_account')
# Q 140 : # Mute.where(account_id: receiver_id, target_account_id: account_ids).any?
Query(Mute)
.where("target_account_id = ?")
# Q 141 : # Mute.where(account_id: receiver_id, target_account_id: account_ids, hide_notifications: true).any?
Query(Mute)
.where("target_account_id = ?")
.where("hide_notifications = ?")
# Q 142 : # Mute.where(account_id: receiver_id, target_account_id: check_for_blocks).pluck(:target_account_id).each_with_object({ })
Query(Mute)
.where("target_account_id = ?")
.select('target_account_id')
# Q 143 : # Mute.where(target_account_id: target_account_ids, account_id: account_id).each_with_object({ })
Query(Mute)
.where("target_account_id = ?")
# Q 144 : # Poll.attached.find(params[:id])
Query(Poll)
.where("id = ?")
# Q 145 : # Poll.attached.find(params[:poll_id])
Query(Poll)
.where("id = ?")
# Q 146 : # Relay.find(params[:id])
Query(Relay)
.where("id = ?")
# Q 147 : # Relay.find_by(follow_activity_id: object_uri)
Query(Relay)
.where("follow_activity_id = ?")
# Q 148 : # Relay.find_by(follow_activity_id: object_uri)
Query(Relay)
.where("follow_activity_id = ?")
# Q 149 : # Relay.find_by(inbox_url: @account.inbox_url).enabled?
Query(Relay)
.where("inbox_url = ?")
# Q 150 : # Relay.find_by(inbox_url: @options[:relayed_through_account].inbox_url).enabled?
Query(Relay)
.where("inbox_url = ?")
# Q 151 : # Report.find(params[:id])
Query(Report)
.where("id = ?")
# Q 152 : # Report.find(params[:id])
Query(Report)
.where("id = ?")
# Q 153 : # Report.find(params[:report_id])
Query(Report)
.where("id = ?")
# Q 154 : # Report.find(report_id)
Query(Report)
.where("id = ?")
# Q 156 : # Report.where(target_account: Account.where(domain: params[:id])).count
Query(Report)
.where("target_account = ?")
# Q 157 : # Report.where(target_account: account).unresolved.where("? = ANY(status_ids)", id).exists?
Query(Report)
.where("target_account = ?")
.return_limit('1')
# Q 158 : # Report.where(target_account: target_account).unresolved
Query(Report)
.where("target_account = ?")
# Q 159 : # Report.where(target_account_id: value)
Query(Report)
.where("target_account_id = ?")
# Q 160 : # Report.where.not(id: id).where(target_account_id: target_account_id).unresolved.exists?
Query(Report)
.where("id = ?")
.where("target_account_id = ?")
.return_limit('1')
# Q 161 : # ReportFilter.new(filter_params).results.order(id: :desc).includes(:account, :target_account)
Query(ReportFilter)
.order('id')
# Q 162 : # ReportNote.find(params[:id])
Query(ReportNote)
.where("id = ?")
# Q 163 : # SessionActivation.find_by(session_id: cookies.signed["_session_id"])
Query(SessionActivation)
.where("session_id = ?")
# Q 164 : # Setting.unscoped.where(thing_type: @object.class.base_class.to_s, thing_id: @object.id)
Query(Setting)
.where("thing_type = ?")
.where("thing_id = ?")
# Q 165 : # Setting.where(var: key).first_or_initialize(var: key)
Query(Setting)
.where("var = ?")
# Q 166 : # SiteUpload.where(var: key).first_or_initialize(var: key)
Query(SiteUpload)
.where("var = ?")
# Q 167 : # Status.find(params[:id])
Query(Status)
.where("id = ?")
# Q 168 : # Status.find(params[:id])
Query(Status)
.where("id = ?")
# Q 169 : # Status.find(params[:status_id])
Query(Status)
.where("id = ?")
# Q 170 : # Status.find(params[:status_id])
Query(Status)
.where("id = ?")
# Q 171 : # Status.find(params[:status_id])
Query(Status)
.where("id = ?")
# Q 172 : # Status.find(params[:status_id])
Query(Status)
.where("id = ?")
# Q 173 : # Status.find(params[:status_id])
Query(Status)
.where("id = ?")
# Q 174 : # Status.find(recognized_params[:id])
Query(Status)
.where("id = ?")
# Q 175 : # Status.find_by(account: @account, reblog: original_status)
Query(Status)
.where("account = ?")
.where("reblog = ?")
# Q 176 : # Status.find_by(id: matches[2])
Query(Status)
.where("id = ?")
# Q 177 : # Status.find_by(uri: @object["atomUri"])
Query(Status)
.where("uri = ?")
# Q 178 : # Status.find_by(uri: @object["atomUri"], account: @account)
Query(Status)
.where("uri = ?")
.where("account = ?")
# Q 179 : # Status.find_by(uri: @object["atomUri"], account: @account)
Query(Status)
.where("uri = ?")
.where("account = ?")
# Q 180 : # Status.find_by(uri: object_uri, account: @account)
Query(Status)
.where("uri = ?")
.where("account = ?")
# Q 181 : # Status.find_by(uri: object_uri, account: @account)
Query(Status)
.where("uri = ?")
.where("account = ?")
# Q 182 : # Status.find_by(uri: object_uri, account_id: @account.id)
Query(Status)
.where("uri = ?")
.where("account_id = ?")
# Q 183 : # Status.remote.where("id < ?", max_id).where(reblog_of_id: nil).where(in_reply_to_id: nil).where("id NOT IN (SELECT status_pins.status_id FROM status_pins WHERE statuses.id = status_id)").where("id NOT IN (SELECT mentions.status_id FROM mentions WHERE statuses.id = mentions.status_id AND mentions.account_id IN (SELECT accounts.id FROM accounts WHERE domain IS NULL))").where("id NOT IN (SELECT statuses1.in_reply_to_id FROM statuses AS statuses1 WHERE statuses.id = statuses1.in_reply_to_id)").where("id NOT IN (SELECT statuses1.reblog_of_id FROM statuses AS statuses1 WHERE statuses.id = statuses1.reblog_of_id AND statuses1.account_id IN (SELECT accounts.id FROM accounts WHERE accounts.domain IS NULL))").where("account_id NOT IN (SELECT follows.target_account_id FROM follows WHERE statuses.account_id = follows.target_account_id)").in_batches.delete_all
Query(Status)
.where("reblog_of_id = ?")
# Q 184 : # Status.where(account_id: user.account).find(params[:id])
Query(Status)
.where("account_id = ?")
.where("id = ?")
# Q 185 : # Status.where(id: account_media_status_ids)
Query(Status)
.where("id = ?")
# Q 186 : # Status.where(id: account_media_status_ids)
Query(Status)
.where("id = ?")
# Q 187 : # Status.where(id: ids).includes(:account)
Query(Status)
.where("id = ?")
.includes('account')
# Q 188 : # Status.where(id: media_attached_status_ids).reorder(nil).find_each
Query(Status)
.where("id = ?")
# Q 189 : # Status.where(id: status_ids).reorder(nil).find_each
Query(Status)
.where("id = ?")
# Q 190 : # Status.where(id: timeline_status_ids, account: target_account)
Query(Status)
.where("id = ?")
.where("account = ?")
# Q 191 : # Status.where(id: unhydrated).cache_ids
Query(Status)
.where("id = ?")
# Q 192 : # Status.where(reblog_of_id: @status.id).where(visibility: [:public, :unlisted]).paginate_by_max_id(limit_param(DEFAULT_ACCOUNTS_LIMIT), params[:max_id], params[:since_id])
Query(Status)
.where("reblog_of_id = ?")
.where("visibility = ?")
# Q 193 : # Status.where(visibility: %i{public unlisted}).where(id: matching_status_ids).pluck(:id)
Query(Status)
.where("visibility = ?")
.where("id = ?")
.select('id')
# Q 194 : # Status.with_discarded.where(id: status_ids).includes(:account, :media_attachments, :mentions)
Query(Status)
.where("id = ?")
.includes('account')
.includes('media_attachments')
.includes('mentions')
# Q 195 : # StatusPin.find_by(account: @account, status: status)
Query(StatusPin)
.where("account = ?")
.where("status = ?")
# Q 196 : # StatusPin.find_by(account: current_account, status: @status)
Query(StatusPin)
.where("account = ?")
.where("status = ?")
# Q 197 : # StatusPin.select("status_id").where(status_id: status_ids).where(account_id: account_id).each_with_object({ })
Query(StatusPin)
.select('status_id')
.where("status_id = ?")
.where("account_id = ?")
# Q 198 : # Tag.discoverable.find_normalized!(params[:id])
Query(Tag)

# Q 199 : # Tag.find(params[:id])
Query(Tag)
.where("id = ?")
# Q 200 : # Tag.most_used(current_account).where.not(id: @featured_tags.map(&:id)).limit(10)
Query(Tag)
.where("id = ?")
.return_limit('10')
# Q 201 : # Tag.most_used(current_account).where.not(id: current_account.featured_tags).limit(10)
Query(Tag)
.where("id = ?")
.return_limit('10')
# Q 202 : # Tag.order("last_status_at DESC NULLS LAST")
Query(Tag)
.order('id, last_status_at')
# Q 203 : # Tag.order("max_score DESC NULLS LAST")
Query(Tag)
.order('id, max_score')
# Q 204 : # Tag.pending_review.order(requested_review_at: :desc)
Query(Tag)
.order('requested_review_at')
# Q 205 : # Tag.reviewed.order(reviewed_at: :desc)
Query(Tag)
.order('reviewed_at')
# Q 206 : # Tag.usable.find_normalized!(params[:id])
Query(Tag)
.select('usable')
# Q 207 : # Tag.where(id: tag_ids)
Query(Tag)
.where("id = ?")
# Q 208 : # Tag.where(id: tag_ids)
Query(Tag)
.where("id = ?")
# Q 209 : # Tag.where(id: tag_ids.uniq)
Query(Tag)
.where("id = ?")
# Q 210 : # User.confirmed.recent.includes(:account).limit(8)
Query(User)
.includes('account')
.return_limit('10')
# Q 211 : # User.find(doorkeeper_token.resource_owner_id)
Query(User)
.where("id = ?")
# Q 212 : # User.find(params[:user_id])
Query(User)
.where("id = ?")
# Q 213 : # User.find(session[:otp_user_id])
Query(User)
.where("id = ?")
# Q 214 : # User.find_by(email: email)
Query(User)
.where("email = ?")
# Q 215 : # User.pending.find_each(&:approve!)
Query(User)

# Q 216 : # User.pending.limit(options[:number]).each(&:approve!)
Query(User)
.return_limit('10')
# Q 217 : # User.staff.includes(:account).each
Query(User)
.includes('account')
# Q 218 : # User.staff.includes(:account).to_a.select(&:allows_trending_tag_emails?)
Query(User)
.includes('account')
# Q 219 : # account.active_relationships.includes(:target_account).reorder(id: :desc).each
Query(Account)
.order('id')
# Q 220 : # account.blocking.select(:username, :domain)
Query(Account)
.select('username')
.select('domain')
# Q 221 : # account.domain_blocks.pluck(:domain).each
Query(Account)
.select('domain')
# Q 222 : # account.last_webfingered_at
Query(Account)
.select('last_webfingered_at')
# Q 223 : # account.last_webfingered_at.present?
Query(Account)
.select('last_webfingered_at')
# Q 224 : # account.mute_relationships.includes(:target_account).reorder(id: :desc).each
Query(Account)
.order('id')
# Q 226 : # account.statuses.where(in_reply_to_id: id, visibility: [:public, :unlisted]).reorder(id: :asc).limit(limit)
Query(Account)
.joins('statuses')
.where("statuses.visibility = ?")
.order('id')
.return_limit('10')
# Q 227 : # account.statuses.where(visibility: %i{public unlisted}).tagged_with(tag).count
Query(Account)
.joins('statuses')
.where("statuses.visibility = ?")
# Q 228 : # account.statuses.where(visibility: %i{public unlisted}).tagged_with(tag).select(:created_at).first.created_at
Query(Account)
.joins('statuses')
.where("statuses.visibility = ?")
.select('created_at')
.return_limit('1')
.select('created_at')
# Q 231 : # accounts.pluck("distinct domain").compact
Query(Account)
.select('domain')
.where("id != 0")
# Q 232 : # accounts.where(silenced_at: created_at)
Query(Account)
.where("silenced_at = ?")
# Q 233 : # accounts.where(suspended_at: created_at)
Query(Account)
.where("suspended_at = ?")
# Q 234 : # confirmed.enabled.joins(:account).merge(Account.searchable)
Query(User)
.joins('account')
# Q 235 : # confirmed.where(arel_table[:current_sign_in_at].gteq(ACTIVE_DURATION.ago)).joins(:account).where(accounts: { suspended_at: nil })
Query(User)
.joins('account')
.where("account.suspended_at = ?")
# Q 236 : # conversation_mutes.find_by(conversation: conversation)
Query(ConversationMute)
.where("conversation = ?")
# Q 237 : # conversation_mutes.where(conversation: conversation).exists?
Query(ConversationMute)
.where("conversation = ?")
.return_limit('1')
# Q 238 : # user.account.statuses.where(reblog_of_id: params[:status_id]).first!
Query(Account)
.joins('statuses')
.where("id = ?")
.where("statuses.reblog_of_id = ?")
.return_limit('1')
# Q 240 : # user.invites.order(id: :desc)
Query(Invite)
.where("user_id = ?")
.order('id')
# Q 241 : # user.session_activations.find(params[:id])
Query(SessionActivation)
.where("user_id = ?")
.where("id = ?")
# Q 242 : # domain_blocks.find_by(domain: other_domain)
Query(DomainBlock)
.where("domain = ?")
# Q 243 : # domain_blocks.pluck(:domain)
Query(DomainBlock)
.select('domain')
# Q 244 : # domain_blocks.where(domain: other_domain).exists?
Query(DomainBlock)
.where("domain = ?")
.return_limit('1')
# Q 245 : # favourites.where(account: Account.local).pluck(:account_id)
Query(Favourite)
.where("account = ?")
.select('account_id')
# Q 246 : # find_by(account: recipient, conversation_id: status.conversation_id, participant_account_ids: participants_from_status(recipient, status))
Query(AccountConversation)
.where("account = ?")
.where("conversation_id = ?")
# Q 247 : # find_by(domain: uri.normalized_host)
Query(DomainAllow)
.where("domain = ?")
# Q 248 : # follow_requests.where(target_account: other_account).exists?
Query(FollowRequest)
.where("target_account = ?")
.return_limit('1')
# Q 249 : # group(:domain).select(:domain, "COUNT(*) AS accounts_count").order("accounts_count desc")
Query(Account)
.group('domain')
.order('id')
# Q 250 : # invites.find(params[:id])
Query(Invite)
.where("id = ?")
# Q 252 : # joins(:statuses).where(statuses: { account: account }).group(:id).order("count(*) desc")
Query(Tag)
.joins('statuses')
.where("statuses.account = ?")
.group('id')
.order('id')
# Q 254 : # left_outer_joins(:account).where(accounts: { silenced_at: nil })
Query(Status)
.left_outer_joins('account')
.where("account.silenced_at = ?")
# Q 255 : # left_outer_joins(:account).where.not(accounts: { silenced_at: nil })
Query(Status)
.left_outer_joins('account')
.where("account.silenced_at = ?")
# Q 256 : # left_outer_joins(:reblog)
Query(Status)
.left_outer_joins('reblog')
# Q 257 : # list.accounts.select(:username, :domain).each
Query(Account)
.select('username')
.select('domain')
# Q 258 : # listable.joins(:account_tag_stat).where(AccountTagStat.arel_table[:accounts_count].gt(0)).order("account_tag_stats.accounts_count desc")
Query(Tag)
.joins('account_tag_stat')
.order('id')
# Q 259 : # lists.joins(account: :user).where("users.current_sign_in_at > ?", User::ACTIVE_DURATION.ago)
Query(List)

# Q 260 : # local.where(disabled: false).where(visible_in_picker: true)
Query(CustomEmoji)
.where("disabled = ?")
.where("visible_in_picker = ?")
# Q 261 : # mentions.includes(:account).map(&:account)
Query(Mention)
.includes('account')
# Q 262 : # mentions.where(account: Account.local).pluck(:account_id)
Query(Mention)
.where("account = ?")
.select('account_id')
# Q 263 : # options.fetch(:file_geometry_parser).from_file(@file)
Query(Option)

# Q 264 : # order("account_stats.followers_count desc")
Query(Account)
.order('id')
# Q 265 : # order("(CASE severity WHEN 0 THEN 1 WHEN 1 THEN 2 WHEN 2 THEN 0 END), reject_media, domain")
Query(DomainBlock)
.order('id, reject_media, domain, severity')
# Q 266 : # order("(case when account_stats.last_status_at is null then 1 else 0 end) asc, account_stats.last_status_at desc, accounts.id desc")
Query(Account)
.order('id')
# Q 267 : # order("row_number() over (partition by domain)")
Query(Account)
.order('id, domain')
# Q 268 : # order(arel_table[:last_status_id].asc).limit(limit)
Query(AccountConversation)
.order('last_status_id')
.return_limit('10')
# Q 269 : # order(arel_table[:last_status_id].desc).limit(limit)
Query(AccountConversation)
.order('last_status_id')
.return_limit('10')
# Q 270 : # order(created_at: :desc)
Query(AccountWarning)
.order('created_at')
# Q 271 : # order(domain: :asc, shortcode: :asc)
Query(CustomEmoji)
.order('domain, shortcode')
# Q 272 : # order(domain: :asc, username: :asc)
Query(Account)
.order('domain, username')
# Q 273 : # order(id: :desc)
Query(User)
.order('id')
# Q 274 : # poll.votes.where(account: @account).exists?
Query(PollVote)
.where("poll_id = ?")
.where("account = ?")
.return_limit('1')
# Q 275 : # remote.where.not(subscription_expires_at: nil).where("subscription_expires_at < ?", time)
Query(Account)
.where("subscription_expires_at = ?")
# Q 276 : # reorder("created_at DESC")
Query(AccountModerationNote)
.order('id, created_at')
# Q 277 : # reorder(created_at: :desc)
Query(ReportNote)
.order('created_at')
# Q 278 : # reorder(id: :desc)
Query(Status)
.order('id')
# Q 279 : # reorder(id: :desc)
Query(Account)
.order('id')
# Q 280 : # reorder(id: :desc)
Query(Follow)
.order('id')
# Q 283 : # searchable.without_silenced.where(discoverable: true).left_outer_joins(:account_stat)
Query(Account)
.where("discoverable = ?")
# Q 284 : # select(:id, :updated_at, :activity_type, :activity_id)
Query(Notification)
.select('id')
.select('updated_at')
.select('activity_type')
.select('activity_id')
# Q 285 : # status.account.followers.where(id: account_ids).map
Query(Account)
.where("id = ?")
.where("id = ?")
# Q 286 : # status.active_mentions.includes(:account).each
Query(Mention)
.where("status_id = ?")
.includes('account')
# Q 287 : # status.active_mentions.pluck(:account_id)
Query(Mention)
.where("status_id = ?")
.select('account_id')
# Q 288 : # status.active_mentions.pluck(:account_id)
Query(Mention)
.where("status_id = ?")
.select('account_id')
# Q 289 : # status.active_mentions.pluck(:account_id)
Query(Mention)
.where("status_id = ?")
.select('account_id')
# Q 290 : # status.favourites.where(account: @account).first
Query(Favourite)
.where("status_id = ?")
.where("account = ?")
.return_limit('1')
# Q 291 : # status.preloadable_poll
Query(Poll)
.where("id = ?")
# Q 292 : # status.preloadable_poll
Query(Poll)
.where("id = ?")
# Q 293 : # status.preloadable_poll
Query(Poll)
.where("id = ?")
# Q 294 : # status.preloadable_poll.nil?
Query(Poll)
.where("id = ?")
# Q 295 : # status.preloadable_poll.options.map { |o|
#   
#   "[ ] #{
#   o}"
# }.join("\n")
Query(Poll)
.where("id = ?")
.select('options')
# Q 296 : # status.preloadable_poll.options.map { |title|
#   
#   "[ ] #{
#   title}"
# }.join("\n")
Query(Poll)
.where("id = ?")
.select('options')
# Q 297 : # status.proper.favourites.where(account: self).exists?
Query(Favourite)
.where("status_id = ?")
.where("account = ?")
.return_limit('1')
# Q 298 : # status.proper.reblogs.where(account: self).exists?
Query(Status)
.where("account = ?")
.return_limit('1')
# Q 299 : # status.replies.where.not(visibility: :direct).count
Query(Status)
.where("visibility = ?")
# Q 300 : # status_pins.where(status: status).exists?
Query(StatusPin)
.where("status = ?")
.return_limit('1')
# Q 301 : # statuses.joins(:media_attachments).distinct(:id).pluck(:id)
Query(Status)
.joins('media_attachments')
.distinct('')
.select('id')
# Q 302 : # statuses.joins(:media_attachments).distinct(:id).pluck(:id)
Query(Status)
.joins('media_attachments')
.distinct('')
.select('id')
# Q 303 : # statuses.map(&:account_domain).compact.uniq
Query(Status)
.where("id != 0")
.distinct('')
# Q 304 : # statuses.map(&:account_id).uniq
Query(Status)
.distinct('')
# Q 305 : # statuses.where(id: status_ids)
Query(Status)
.where("id = ?")
# Q 306 : # statuses.where(id: status_ids)
Query(Status)
.where("id = ?")
# Q 307 : # tag.last_status_at
Query(Tag)
.select('last_status_at')
# Q 308 : # tag.last_status_at.nil?
Query(Tag)
.select('last_status_at')
# Q 309 : # where("statuses.reblog_of_id IS NULL")
Query(Status)

# Q 310 : # where("statuses.reply = FALSE OR statuses.in_reply_to_account_id = statuses.account_id")
Query(Status)

# Q 311 : # where(account: account, visibility: :public)
Query(Status)
.where("account = ?")
.where("visibility = ?")
# Q 312 : # where(action_taken: false)
Query(Report)
.where("action_taken = ?")
# Q 313 : # where(action_taken: true)
Query(Report)
.where("action_taken = ?")
# Q 314 : # where(actor_type: %w{Application Service})
Query(Account)
.where("actor_type = ?")
# Q 315 : # where(approved: false)
Query(User)
.where("approved = ?")
# Q 316 : # where(approved: true)
Query(User)
.where("approved = ?")
# Q 317 : # where(disabled: false)
Query(User)
.where("disabled = ?")
# Q 318 : # where(disabled: true)
Query(User)
.where("disabled = ?")
# Q 319 : # where(domain: domain).or(where(arel_table[:domain].matches("%." + domain)))
Query(Account)
.where("domain = ?")
# Q 320 : # where(domain: domain).or(where(arel_table[:domain].matches("%." + domain)))
Query(CustomEmoji)
.where("domain = ?")
# Q 321 : # where(domain: nil)
Query(Account)
.where("domain = ?")
# Q 322 : # where(domain: nil)
Query(CustomEmoji)
.where("domain = ?")
# Q 323 : # where(domain: variants[0..-2]).order("char_length(domain) desc").first
Query(DomainBlock)
.where("domain = ?")
.order('id, domain')
.return_limit('1')
# Q 324 : # where(expires_at: nil).or(where("expires_at >= ?", Time.now.utc))
Query(Invite)
.where("expires_at = ?")
# Q 325 : # where(irreversible: true).where("expires_at IS NULL OR expires_at > NOW()")
Query(CustomFilter)
.where("irreversible = ?")
# Q 326 : # where(language: account.chosen_languages)
Query(Status)
.where("language = ?")
# Q 327 : # where(language: nil)
Query(Status)
.where("language = ?")
# Q 328 : # where(listable: [true, nil])
Query(Tag)
.where("listable = ?")
# Q 329 : # where(local: false).where.not(uri: nil)
Query(Status)
.where("local = ?")
.where("uri = ?")
# Q 330 : # where(local: true).or(where(uri: nil))
Query(Status)
.where("local = ?")
# Q 331 : # where(remote_url: "")
Query(MediaAttachment)
.where("remote_url = ?")
# Q 332 : # where(reviewed_at: nil)
Query(Tag)
.where("reviewed_at = ?")
# Q 333 : # where(severity: [:silence, :suspend]).or(where(reject_media: true))
Query(DomainBlock)
.where("severity = ?")
# Q 334 : # where(silenced_at: nil)
Query(Account)
.where("silenced_at = ?")
# Q 335 : # where(silent: false)
Query(Mention)
.where("silent = ?")
# Q 336 : # where(silent: true)
Query(Mention)
.where("silent = ?")
# Q 337 : # where(status_id: nil)
Query(Poll)
.where("status_id = ?")
# Q 338 : # where(status_id: nil, scheduled_status_id: nil)
Query(MediaAttachment)
.where("status_id = ?")
.where("scheduled_status_id = ?")
# Q 339 : # where(suspended_at: nil)
Query(Account)
.where("suspended_at = ?")
# Q 340 : # where(usable: [true, nil])
Query(Tag)
.where("usable = ?")
# Q 341 : # where(verified: true, live: true)
Query(AccountIdentityProof)
.where("verified = ?")
.where("live = ?")
# Q 342 : # where(visibility: :public)
Query(Status)
.where("visibility = ?")
# Q 343 : # where(visibility: visibility)
Query(Status)
.where("visibility = ?")
# Q 344 : # where.not(account_id: account.excluded_from_timeline_account_ids)
Query(Status)
.where("account_id = ?")
# Q 345 : # where.not(confirmed_at: nil)
Query(User)
.where("confirmed_at = ?")
# Q 346 : # where.not(domain: nil)
Query(CustomEmoji)
.where("domain = ?")
# Q 347 : # where.not(domain: nil)
Query(Account)
.where("domain = ?")
# Q 348 : # where.not(id: account.excluded_from_timeline_account_ids)
Query(Account)
.where("id = ?")
# Q 349 : # where.not(image_file_name: [nil, ""])
Query(PreviewCard)
.where("image_file_name = ?")
# Q 350 : # where.not(remote_url: "")
Query(MediaAttachment)
.where("remote_url = ?")
# Q 351 : # where.not(reviewed_at: nil)
Query(Tag)
.where("reviewed_at = ?")
# Q 352 : # where.not(silenced_at: nil)
Query(Account)
.where("silenced_at = ?")
# Q 353 : # where.not(status_id: nil)
Query(Poll)
.where("status_id = ?")
# Q 354 : # where.not(status_id: nil).or(where.not(scheduled_status_id: nil))
Query(MediaAttachment)
.where("status_id = ?")
# Q 355 : # where.not(suspended_at: nil)
Query(Account)
.where("suspended_at = ?")
# Q 356 : # where.not(text: "")
Query(AccountWarning)
.where("text = ?")
# Q 357 : # without_suspended.where(moved_to_account_id: nil)
Query(Account)
.where("moved_to_account_id = ?")