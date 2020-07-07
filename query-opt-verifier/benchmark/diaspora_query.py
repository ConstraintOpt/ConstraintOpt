# Q 0 : # @contact.aspect_memberships.first
Query(AspectMembership)
.where("contact_id = ?")
.return_limit('1')
# Q 1 : # @conversation.first_unread_message(user).try(:id)
Query(Conversation)
.select('id')
# Q 2 : # @conversation.first_unread_message(user).try(:id)
Query(Conversation)
.select('id')
# Q 3 : # @conversation.first_unread_message(user).try(:id)
Query(Conversation)
.select('id')
# Q 4 : # @person.posts.where(:public => true)
Query(Post)
.where("author_id = ?")
.where("public = ?")
# Q 5 : # AccountDeletion.find_by(person: person).update_attributes(completed_at: Time.now.utc)
Query(AccountDeletion)
.where("person = ?")
# Q 6 : # AccountDeletion.where(person: person).exists?
Query(AccountDeletion)
.where("person = ?")
.return_limit('1')
# Q 7 : # AccountDeletion.where(person: person).exists?
Query(AccountDeletion)
.where("person = ?")
.return_limit('1')
# Q 8 : # AccountMigration.where(old_person: old_person, new_person: profile.person).exists?
Query(AccountMigration)
.where("old_person_id = ?")
.where("new_person_id = ?")
.return_limit('1')
# Q 9 : # AccountMigration.where(old_person: old_person, new_person: profile.person).exists?
Query(AccountMigration)
.where("old_person_id = ?")
.where("new_person_id = ?")
.return_limit('1')
# Q 10 : # ApiOpenidConnectAuthorization.find_by_client_id_user_and_scopes(client_id, user, params[:scope])
Query(ApiOpenidConnectAuthorization)
.where("o_auth_application = ?")
.where("user = ?")
# Q 11 : # ApiOpenidConnectAuthorization.find_by_client_id_user_and_scopes(params[:client_id], user, params[:scope])
Query(ApiOpenidConnectAuthorization)
.where("o_auth_application = ?")
.where("user = ?")
# Q 12 : # Aspect.joins("INNER JOIN aspects as a2 ON (aspects.name = a2.name AND aspects.user_id=#{
# old_user.id}
#         AND a2.user_id=#{
# newest_user.id})").destroy_all
Query(Aspect)
.joins('aspect')
.where("user_id = ?")

# Q 13 : # Comment.find_by_id(item_id).nil?
Query(Comment)
.where("id = ?")
# Q 14 : # Comment.where.not(author_id: person_id).joins("INNER JOIN posts ON (commentable_type = 'Post' AND posts.id = commentable_id)").where("posts.author_id = ?", person_id)
Query(Comment)
.where("author_id = ?")
# Q 15 : # Contact.all_contacts_of_person(person).find_each(batch_size: 20, &:destroy)
Query(Contact)

# Q 16 : # Contact.includes(person: :profile).find_by(user_id: id, person_id: person_id)
Query(Contact)
.where("user_id = ?")
.where("person_id = ?")
# Q 17 : # Contact.joins(:aspect_memberships).where(aspect_memberships: { aspect: aspects }).distinct.pluck(:person_id)
Query(Contact)
.joins('aspect_memberships')
.where("aspect_memberships.aspect in (?, ?)")
.distinct('')
.select('person_id')
# Q 18 : # Contact.where(:user_id => user.id, :person_id => people.map(&:id)).load
Query(Contact)
.where("user_id = ?")
.where("person_id = ?")
# Q 19 : # Conversation.find(params[:conversation_id])
Query(Conversation)
.where("id = ?")
# Q 20 : # Conversation.find_by_id(self.conversation.id)
Query(Conversation)
.where("id = ?")
# Q 21 : # Conversation.joins(:conversation_visibilities).where(conversation_visibilities: { person_id: user.person_id, conversation_id: params[:conversation_id] }).first
Query(Conversation)
.joins('conversation_visibilities')
.where("conversation_visibilities.person_id = ?")
.return_limit('1')
# Q 22 : # Conversation.where(guid: guid).ids.first
Query(Conversation)
.where("guid = ?")
.return_limit('1')
# Q 23 : # ConversationVisibility.find_by(conversation_id: conversation_id, person_id: user.person.id)
Query(ConversationVisibility)
.where("conversation_id = ?")
.where("person_id = ?")
# Q 24 : # ConversationVisibility.includes(:conversation).order("conversations.updated_at DESC").where(person_id: user.person_id).paginate(page: params[:page], per_page: 15)
Query(ConversationVisibility)
.includes('conversation')
.order('updated_at')
.where("person_id = ?")
# Q 25 : # ConversationVisibility.where(:person_id => user.person.id, :conversation_id => params[:conversation_id]).first
Query(ConversationVisibility)
.where("person_id = ?")
.where("conversation_id = ?")
.return_limit('1')
# Q 26 : # ConversationVisibility.where(person_id: self.person_id).sum(:unread)
Query(ConversationVisibility)
.where("person_id = ?")
# Q 27 : # InvitationCode.find_by_token!(params[:id])
Query(InvitationCode)
.where("token = ?")
# Q 28 : # InvitationCode.find_by_token!(params[:id])
Query(InvitationCode)
.where("token = ?")
# Q 29 : # InvitationCode.find_by_token(params[:invite][:token])
Query(InvitationCode)
.where("token = ?")
# Q 30 : # InvitationCode.find_by_token(params[:invite_code_id]).add_invites!
Query(InvitationCode)
.where("token = ?")
# Q 31 : # Like.find_by(author_id: person.id, target_type: target.class.base_class.to_s, target_id: target.id)
Query(Like)
.where("author_id = ?")
.where("target_type = ?")
.where("target_id = ?")
# Q 32 : # Like.where(:author_id => @user.person_id, :target_id => posts.map(&:id), :target_type => "Post")
Query(Like)
.where("author_id = ?")
.where("target_id = ?")
.where("target_type = ?")
# Q 33 : # Like.where.not(author_id: person_id).joins("INNER JOIN posts ON (target_type = 'Post' AND posts.id = target_id)").where("posts.author_id = ?", person_id)
Query(Like)
.where("author_id = ?")
# Q 34 : # Notification.where(:recipient_id => user.id, :id => params[:id]).first
Query(Notification)
.where("recipient_id = ?")
.where("id = ?")
.return_limit('1')
# Q 35 : # Notification.where(conditions).includes(:target, :actors => :profile).order("updated_at desc").limit(pager.per_page).offset(pager.offset)
Query(Notification)
.includes("target")
.includes('actors')
.order('updated_at')
.return_limit('1')
# Q 36 : # Notification.where(recipient_id: user.id, target_type: "Person", target_id: @person.id, unread: true).each
Query(Notification)
.where("recipient_id = ?")
.where("target_type = ?")
.where("target_id = ?")
.where("unread = ?")
# Q 37 : # Notification.where(recipient_id: user.id, unread: true)
Query(Notification)
.where("recipient_id = ?")
.where("unread = ?")
# Q 38 : # Notification.where(target_type: "Person", target_id: person_id, recipient_id: user_id, type: "NotificationsStartedSharing").destroy_all
Query(Notification)
.where("target_type = ?")
.where("target_id = ?")
.where("recipient_id = ?")
.where("type = ?")
# Q 39 : # Notification.where(target_type: self.class.name, target_id: id).destroy_all
Query(Notification)
.where("target_type = ?")
.where("target_id = ?")
# Q 40 : # NotificationsStartedSharing.where(recipient_id: id, target: person.id, unread: true).update_all(unread: false)
Query(Notification)
.where("recipient_id = ?")
.where("target = ?")
.where("unread = ?")
# Q 41 : # Person.find(aspecting_person_id)
Query(Person)
.where("id = ?")
# Q 42 : # Person.find(params[:person_id])
Query(Person)
.where("id = ?")
# Q 43 : # Person.find_by(diaspora_handle: entity.recipient).owner
Query(Person)
.where("diaspora_handle = ?")
.where("id = ?")
# Q 44 : # Person.find_by(guid: params[:id])
Query(Person)
.where("guid = ?")
# Q 45 : # Person.find_by(guid: params[:person_id])
Query(Person)
.where("guid = ?")
# Q 46 : # Person.find_by_guid!(params[:id])
Query(Person)
.where("guid = ?")
# Q 47 : # Person.includes(:profile).find_by(id: @last_author_id)
Query(Person)
.includes('profile')
.where("id = ?")
# Q 48 : # Person.joins(:contacts).where(contacts: { user_id: person.owner_id })
Query(Person)
.joins('contacts')
.where("contacts.user_id = ?")
# Q 49 : # Person.joins(:roles).where(:roles => { :name => "spotlight" })
Query(Person)
.joins('roles')
.where("roles.name = ?")
# Q 50 : # Person.reflect_on_association(asso).class_name.constantize.where(id: ids).destroy_all
Query(Person)
.where("id = ?")
# Q 51 : # Person.unique_from_aspects(aspect_ids, user).includes(:profile)
Query(Person)
.includes('profile')
# Q 52 : # Person.where(:id => people_ids).includes(:profile)
Query(Person)
.where("id = ?")
.includes('profile')
# Q 53 : # Person.where(diaspora_handle: search_query.downcase, closed_account: false)
Query(Person)
.where("diaspora_handle = ?")
.where("closed_account = ?")
# Q 54 : # Person.where(diaspora_handle: search_query.downcase, closed_account: false)
Query(Person)
.where("diaspora_handle = ?")
.where("closed_account = ?")
# Q 55 : # Person.where(guid: guid).where.not(diaspora_handle: diaspora_handle).pluck(:diaspora_handle).first
Query(Person)
.where("guid = ?")
.where("diaspora_handle = ?")
.select('diaspora_handle')
.return_limit('1')
# Q 56 : # Person.where(id: comments.select(:author_id).distinct)
Query(Person)
.where("id = ?")
# Q 57 : # Person.where(id: opts[:subscriber_ids])
Query(Person)
.where("id = ?")
# Q 58 : # Person.where(id: person_id).first
Query(Person)
.where("id = ?")
.return_limit('1')
# Q 59 : # Photo.where(:author_id => user.person_id, :id => params[:photo_id]).first
Query(Photo)
.where("author_id = ?")
.where("id = ?")
.return_limit('1')
# Q 60 : # Photo.where(author_id: person.id, public: true)
Query(Photo)
.where("author_id = ?")
.where("public = ?")
# Q 61 : # Photo.where(id: params[:id], public: true).first
Query(Photo)
.where("id = ?")
.where("public = ?")
.return_limit('1')
# Q 62 : # Photo.where(id: params[:photo_id], author_id: author_id).first
Query(Photo)
.where("id = ?")
.where("author_id = ?")
.return_limit('1')
# Q 63 : # Pod.find(params[:pod_id])
Query(Pod)
.where("id = ?")
# Q 64 : # Pod.find(subscribers.select(&:remote?).map(&:pod_id).uniq).map
Query(Pod)
.where("id = ?")
# Q 65 : # Pod.where(id: people.map(&:pod_id).uniq).partition(&:active?)
Query(Pod)
.where("id = ?")
# Q 66 : # Pod.where(scheduled_check: true).find_each(&:test_connection!)
Query(Pod)
.where("scheduled_check = ?")
# Q 67 : # PollAnswer.find(params[:poll_answer_id])
Query(PollAnswer)
.where("id = ?")
# Q 68 : # PollAnswer.where(guid: new_poll_answer_guid).ids.first
Query(PollAnswer)
.where("guid = ?")
.return_limit('1')
# Q 69 : # PollParticipation.where(author_id: self.author.id, poll_id: self.poll.id).to_a
Query(PollParticipation)
.where("author_id = ?")
.where("poll_id = ?")
# Q 70 : # PollParticipation.where.not(author_id: person_id).joins(:status_message).where("posts.author_id = ?", person_id)
Query(PollParticipation)
.where("author_id = ?")
.joins('status_message')
# Q 71 : # Post.all_public.where(:author_id => fetch_ids!(Person.community_spotlight, "people.id"))
Query(Post)
.where("author_id = ?")
# Q 72 : # Post.find_by_guid(post["guid"]).blank?
Query(Post)
.where("guid = ?")
# Q 73 : # Post.find_by_id(item_id).nil?
Query(Post)
.where("id = ?")
# Q 74 : # Post.from_person_visible_by_user(self, person).order("posts.created_at desc")
Query(Post)
.order('created_at')
# Q 75 : # Post.where("created_at >= ?", Date.today - 21.days).group("DATE(created_at)").order("DATE(created_at) ASC").count
Query(Post)
.group('id, created_at')
.order('created_at')
# Q 76 : # Post.where(:id => post_ids)
Query(Post)
.where("id = ?")
# Q 77 : # Post.where(author_id: @user.person_id, public: true).order("created_at DESC").limit(25).map { |post|
#   
#   post.is_a?(Reshare) ? post.absolute_root : post
# }.compact
Query(Post)
.where("author_id = ?")
.where("public = ?")
.order('created_at')
.return_limit('1')
.where("id != 0")
# Q 78 : # Profile.where(:image_url => url(:thumb_large))
Query(Profile)
.where("image_url = ?")
# Q 79 : # Report.where(id: params[:id]).first
Query(Report)
.where("id = ?")
.return_limit('1')
# Q 80 : # Report.where(id: params[:id]).first
Query(Report)
.where("id = ?")
.return_limit('1')
# Q 81 : # Report.where(item_id: item_id, item_type: item_type).exists?(user_id: user_id)
Query(Report)
.where("item_id = ?")
.where("item_type = ?")
.return_limit('1')
# Q 82 : # Report.where(item_id: item_id, item_type: item_type).update_all(reviewed: true)
Query(Report)
.where("item_id = ?")
.where("item_type = ?")
# Q 83 : # Report.where(reviewed: false)
Query(Report)
.where("reviewed = ?")
# Q 84 : # Report.where(reviewed: false).size
Query(Report)
.where("reviewed = ?")
# Q 85 : # Reshare.where(author_id: user.person_id, root_guid: absolute_root.guid).first
Query(Reshare)
.where("author_id = ?")
.where("root_guid = ?")
.return_limit('1')
# Q 86 : # Role.admins.first.person.owner
Query(User)
.return_limit('1')
.where("id = ?")
.where("id = ?")
# Q 87 : # Service.where(uid: omniauth_hash["uid"]).first
Query(Service)
.where("uid = ?")
.return_limit('1')
# Q 88 : # ShareVisibility.for_a_user(user).find_each(batch_size: 20, &:destroy)
Query(ShareVisibility)

# Q 89 : # ShareVisibility.for_shareable(share).where(user_id: user_ids).pluck(:user_id)
Query(ShareVisibility)
.where("user_id = ?")
.select('user_id')
# Q 90 : # ShareVisibility.where(:hidden => true).includes(:contact => :user)
Query(ShareVisibility)
.where("hidden = ?")
.includes('user')
# Q 91 : # StatusMessage.find_by(guid: photo.status_message_guid)
Query(StatusMessage)
.where("guid = ?")
# Q 92 : # StatusMessage.find_by_guid(self.status_message_guid)
Query(StatusMessage)
.where("guid = ?")
# Q 93 : # StatusMessage.where_person_is_mentioned(@user.person)
Query(StatusMessage)

# Q 94 : # StatusMessage.where_person_is_mentioned(self.user.person)
Query(StatusMessage)

# Q 95 : # User.find(params[:id])
Query(User)
.where("id = ?")
# Q 96 : # User.find(params[:id])
Query(User)
.where("id = ?")
# Q 97 : # User.find(params[:id])
Query(User)
.where("id = ?")
# Q 98 : # User.find(recipient_id).disconnected_by(object)
Query(User)
.where("id = ?")
# Q 99 : # User.find(session[:otp_user_id])
Query(User)
.where("id = ?")
# Q 100 : # User.find_by(username: AppConfig.admins.account.to_s)
Query(User)
.where("username = ?")
# Q 101 : # User.find_by(username: sender_username)
Query(User)
.where("username = ?")
# Q 102 : # User.find_by_email(email)
Query(User)
.where("email = ?")
# Q 103 : # User.find_by_username(AppConfig.admins.account.get)
Query(User)
.where("username = ?")
# Q 104 : # User.find_by_username(params[:username])
Query(User)
.where("username = ?")
# Q 105 : # User.find_by_username(params[:username])
Query(User)
.where("username = ?")
# Q 106 : # User.joins(:contacts).where(:contacts => { :person_id => person.id })
Query(User)
.joins('contacts')
.where("contacts.person_id = ?")
# Q 107 : # User.joins(person: :profile)
Query(User)
.joins('profile')
# Q 108 : # User.reflect_on_association(asso).class_name.constantize.where(id: ids).destroy_all
Query(User)
.where("id = ?")
# Q 109 : # User.where("username IS NOT NULL and created_at IS NOT NULL")
Query(User)

# Q 110 : # User.where(id: params[:id]).first
Query(User)
.where("id = ?")
.return_limit('1')
# Q 111 : # User.where(id: recipient_ids).find_each
Query(User)
.where("id = ?")
# Q 112 : # User.where(id: recipient_ids).find_each
Query(User)
.where("id = ?")
# Q 113 : # User.where(locked_at: nil).first
Query(User)
.where("locked_at = ?")
.return_limit('1')
# Q 114 : # User.where(unconfirmed_email: email).update_all(unconfirmed_email: nil, confirm_email_token: nil)
Query(User)
.where("unconfirmed_email = ?")
# Q 115 : # all_from_aspects(aspect_ids, user).select("DISTINCT people.*")
Query(Person)
.distinct('')
# Q 116 : # aspects.where(:id => aspect_ids).to_a
Query(Aspect)
.where("id = ?")
# Q 117 : # aspects.where(post_default: true).to_a
Query(Aspect)
.where("post_default = ?")
# Q 118 : # blocks.find_by(person_id: person.id)
Query(Block)
.where("person_id = ?")
# Q 119 : # blocks.where(person_id: person.id).exists?
Query(Block)
.where("person_id = ?")
.return_limit('1')
# Q 120 : # contact.aspect_memberships.where(aspect_id: aspect.id).first
Query(AspectMembership)
.where("contact_id = ?")
.where("aspect_id = ?")
.return_limit('1')
# Q 121 : # contacts.includes(person: :profile).order(order)
Query(Contact)
.order('id')
# Q 122 : # conversation_visibilities.find_by(person_id: user.person.id)
Query(ConversationVisibility)
.where("person_id = ?")
# Q 123 : # user.aspects.find(params[:a_id])
Query(Aspect)
.where("user_id = ?")
.where("id = ?")
# Q 124 : # user.aspects.find(params[:a_id])
Query(Aspect)
.where("user_id = ?")
.where("id = ?")
# Q 125 : # user.aspects.find(params[:a_id])
Query(Aspect)
.where("user_id = ?")
.where("id = ?")
# Q 126 : # user.aspects.joins(:aspect_memberships).where(aspect_memberships: { id: params[:id] }).first
Query(Aspect)
.where("user_id = ?")
.joins('aspect_memberships')
.where("id = ?")
.return_limit('1')
# Q 127 : # user.aspects.where(:id => params[:aspect_id]).first
Query(Aspect)
.where("user_id = ?")
.where("id = ?")
.return_limit('1')
# Q 128 : # user.aspects.where(:id => params[:id]).first
Query(Aspect)
.where("user_id = ?")
.where("id = ?")
.return_limit('1')
# Q 129 : # user.aspects.where(:id => params[:id]).first
Query(Aspect)
.where("user_id = ?")
.where("id = ?")
.return_limit('1')
# Q 130 : # user.aspects.where(id: params[:aspect_id]).first
Query(Aspect)
.where("user_id = ?")
.where("id = ?")
.return_limit('1')
# Q 131 : # user.aspects.where(id: params[:id]).first
Query(Aspect)
.where("user_id = ?")
.where("id = ?")
.return_limit('1')
# Q 132 : # user.blocks.find_by(id: params[:id])
Query(Block)
.where("user_id = ?")
.where("id = ?")
# Q 133 : # user.blocks.includes(:person)
Query(Block)
.where("user_id = ?")
.includes('person')
# Q 134 : # user.contacts.joins(:aspect_memberships).where(aspect_memberships: { id: params[:id] }).first
Query(Contact)
.where("user_id = ?")
.joins('aspect_memberships')
.where("id = ?")
.return_limit('1')
# Q 135 : # user.contacts.mutual.where(column => params[recipients_param].split(",")).pluck(:person_id)
Query(Contact)
.where("user_id = ?")
.select('person_id')
# Q 136 : # user.conversations.where(id: params[:conversation_id]).first
Query(Conversation)
.where("author_id = ?")
.where("id = ?")
.return_limit('1')
# Q 137 : # user.conversations.where(id: params[:id]).first
Query(Conversation)
.where("author_id = ?")
.where("id = ?")
.return_limit('1')
# Q 138 : # user.services.find(params[:id])
Query(Service)
.where("user_id = ?")
.where("id = ?")
# Q 139 : # find_by(code: code)
Query(ApiOpenidConnectAuthorization)
.where("code = ?")
# Q 140 : # find_by(diaspora_handle: diaspora_id.strip.downcase)
Query(Person)
.where("diaspora_handle = ?")
# Q 141 : # find_by(o_auth_application: app, refresh_token: refresh_token)
Query(ApiOpenidConnectAuthorization)
.where("o_auth_application = ?")
.where("refresh_token = ?")
# Q 142 : # find_by(o_auth_application: app, user: user)
Query(ApiOpenidConnectAuthorization)
.where("o_auth_application = ?")
.where("user = ?")
# Q 143 : # find_by(type: service_type, uid: options[:uid])
Query(Service)
.where("type = ?")
.where("uid = ?")
# Q 144 : # includes(:aspects, person: :profile).order("profiles.last_name ASC")
Query(Contact)
.includes('aspects')
.includes("person")
.order('person.profile.last_name')
# Q 145 : # includes(:o_embed_cache, :open_graph_cache, { :author => :profile }, :mentions => { :person => :profile })
Query(Post)
.includes('o_embed_cache')
.includes('open_graph_cache')
# Q 146 : # joins(:contacts => :aspect_memberships).where(:contacts => { :user_id => user.id }).where(:aspect_memberships => { :aspect_id => aspect_ids })
Query(Person)
.joins('contacts')
.joins('aspect_memberships')
.where("contacts.user_id = ?")
.where("aspect_memberships.aspect_id = ?")
# Q 147 : # joins(:likes).where(:likes => { :author_id => person.id })
Query(Post)
.where("author_id = ?")
# Q 148 : # joins(:participations).where(participations: { author_id: user.person_id })
Query(Post)
.joins('participations')
.where("author_id = ?")
# Q 149 : # joins(:person).where(people: { closed_account: false })
Query(User)
.joins('person')
.where("person.closed_account = ?")
# Q 150 : # joins(:person).where.not(people: { owner_id: nil })
Query(Mention)
.joins('person')
.where("person.owner_id = ?")
# Q 151 : # joins(:posts).where(:posts => { :root_guid => StatusMessage.guids_for_author(user.person), :type => "Reshare" })
Query(Person)
.joins('posts')
.where("posts.root_guid = ?")
# Q 152 : # joins(:profile => :tags).where(:tags => { :name => tag_name }).where("profiles.searchable IS TRUE")
Query(Person)
.joins('profile')
# Q 153 : # joins(:profile).where("profiles.searchable = true OR contacts.user_id = ?", user.id)
Query(Person)
.joins('profile')
# Q 154 : # joins(:reshares).where(reshares_posts: { author_id: person.id })
Query(Post)
.joins('reshares')
.where("author_id = ?")
# Q 155 : # joins(:status_message).where(posts: { public: true })
Query(Poll)
.joins('status_message')
.where("status_message.public = ?")
# Q 156 : # joins(:taggings).where("taggings.tag_id IN (?)", tag_ids)
Query(StatusMessage)

# Q 157 : # joins(contacts: :aspect_memberships).where(aspect_memberships: { aspect_id: aspect_ids }).distinct
Query(Person)
.joins('contacts')
.joins('aspect_memberships')
.where("aspect_memberships.aspect_id = ?")
.distinct('')
# Q 158 : # left_join_visible_post_interactions_on_authorship(post.id).joins("LEFT OUTER JOIN contacts ON people.id = contacts.person_id AND contacts.user_id = #{
# user.id}").joins(:profile).select("        people.id = #{
# unscoped {
#   
#   post.author_id
# }} AS is_author,
#         comments.id IS NOT NULL AS is_commenter,
#         likes.id IS NOT NULL AS is_liker,
#         contacts.id IS NOT NULL AS is_contact
# ").order("        is_author DESC,
#         is_commenter DESC,
#         is_liker DESC,
#         is_contact DESC,
#         profiles.full_name,
#         people.diaspora_handle
# ")
Query(Person)
.joins('profile')
.joins('comments')
.joins('likes')
.select('id')
.select('comments.id')
.select('likes.id')
# Q 159 : # likes.find_by(author_id: user.person.id)
Query(Like)
.where("author_id = ?")
# Q 160 : # mentions.includes(:person).merge(Person.allowed_to_be_mentioned_in_a_comment_to(mentionable.parent))
Query(Mention)
.includes('person')
# Q 161 : # mentions.includes(person: :profile).map(&:person)
Query(Mention)

# Q 162 : # mentions.where(person: Person.where(owner_id: recipient_user_ids).ids)
Query(Mention)
.where("person = ?")
# Q 163 : # message.conversation.participants.local.where.not(id: message.author_id).pluck(:owner_id)
Query(Person)
.where("id != ?")
.includes("conversations")
.where("conversations.messages.id = ?")
.where("id = ?")
.select('owner_id')
# Q 164 : # messages.pluck(:author_id).last
Query(Message)
.select('author_id')
.return_limit('1')
# Q 165 : # notifications.where(:unread => true)
Query(Notification)
.where("unread = ?")
# Q 166 : # notifications.where(type: current_type)
Query(Notification)
.where("type = ?")
# Q 167 : # owned_or_visible_by_user(person.owner).joins(:mentions).where(mentions: { person_id: person.id })
Query(StatusMessage)
# Q 168 : # participations.find_by(target_id: target)
Query(Participation)
.where("target_id = ?")
# Q 169 : # people.find
Query(Person)
.where("id = ?")
# Q 170 : # people.where("people.owner_id IS NOT NULL")
Query(Person)

# Q 171 : # people.where(:owner_id => nil)
Query(Person)
.where("owner_id = ?")
# Q 172 : # photo.status_message.photos.order(:created_at)
Query(Photo)
.where("id = ?")
.where("status_message_id = ?")
.order('created_at')
# Q 173 : # photos.where(pending: false).order("created_at DESC")
Query(Photo)
.where("pending = ?")
.order('created_at')
# Q 174 : # poll_participations.find_by(author_id: user.person.id)
Query(PollParticipation)
.where("author_id = ?")
# Q 175 : # posts.find
Query(Post)
.where("id = ?")
# Q 176 : # posts.find
Query(Post)
.where("id = ?")
# Q 177 : # reshares.find_by(author_id: user.person.id)
Query(Reshare)
.where("author_id = ?")
# Q 178 : # select("DISTINCT posts.*").joins(:comments).where(:comments => { :author_id => person.id })
Query(Post)
.distinct('')
.joins('comments')
.where("comments.author_id = ?")
# Q 179 : # select("people.id, people.guid, people.diaspora_handle").includes(:profile)
Query(Person)
.select('id, guid, diaspora_handle')
.includes('profile')
# Q 180 : # self.class.where(id: id).update_all(reshares_count: reshares.count)
Query(Post)
.where("id = ?")
# Q 181 : # self.conversation_visibilities.where(:person_id => user.person.id).where("unread > 0").first
Query(ConversationVisibility)
.where("conversation_id = ?")
.where("person_id = ?")
.return_limit('1')
# Q 182 : # self.for_visible_shareable_sql(max_time, order).includes_for_a_stream
Query(Post)

# Q 183 : # self.user_preferences.find_or_create_by(email_type: key)
Query(UserPreference)
.where("user_id = ?")
# Q 184 : # self.user_preferences.find_or_create_by(email_type: x)
Query(UserPreference)
.where("user_id = ?")
# Q 185 : # sharing.where(receiving: false)
Query(Contact)
.where("receiving = ?")
# Q 186 : # signature_order.order.split
Query(SignatureOrder)
.select('order')
# Q 187 : # user.aspects.create!(group.slice("name", "chat_enabled"))
Query(Aspect)
.where("user_id = ?")
# Q 188 : # user.aspects.find_by(name: group_name)
Query(Aspect)
.where("user_id = ?")
.where("name = ?")
# Q 189 : # user.aspects.find_by(name: name)
Query(Aspect)
.where("user_id = ?")
.where("name = ?")
# Q 190 : # user.blocks.where(person_id: person_id).exists?
Query(Block)
.where("user_id = ?")
.where("person_id = ?")
.return_limit('1')
# Q 191 : # user.visible_shareables(Post, :all_aspects? => for_all_aspects?, :by_members_of => aspect_ids, :type => TYPES_OF_POST_IN_STREAM, :order => "#{
# order} DESC", :max_time => max_time)
Query(User)

# Q 192 : # user_preferences.find_by(email_type: key)
Query(UserPreference)
.where("email_type = ?")
# Q 193 : # where("completed_at is null")
Query(AccountDeletion)

# Q 194 : # where("expires_at >= ?", time)
Query(ApiOpenidConnectOAuthAccessToken)
.where("expires_at >= ?")

# Q 195 : # where("last_seen > ?", time)
Query(User)

# Q 196 : # where("name LIKE ?", "#{
# name.downcase}%").order("name ASC")
Query(ActsAsTaggableOnTag)
.where("name = ?")
.order('name')
# Q 197 : # where("people.owner_id IS NOT NULL")
Query(Person)

# Q 198 : # where("people.owner_id IS NULL")
Query(Person)

# Q 199 : # where(:status_message_guid => post_guids)
Query(Photo)
.where("status_message_guid = ?")
# Q 200 : # where(name: "admin")
Query(Role)
.where("name = ?")
# Q 201 : # where(name: %w{moderator admin})
Query(Role)
.where("name = ?")
# Q 202 : # where(opts.merge!(recipient_id: recipient.id)).order("updated_at DESC")
Query(Notification)
.order('updated_at')
# Q 203 : # where(person_id: x.id)
Query(Contact)
.where("person_id = ?")
# Q 204 : # where(public: true)
Query(Post)
.where("public = ?")
# Q 205 : # where(receiving: true)
Query(Contact)
.where("receiving = ?")
# Q 206 : # where(shareable_id: shareable.id, shareable_type: shareable.class.base_class.to_s)
Query(ShareVisibility)
.where("shareable_id = ?")
.where("shareable_type = ?")
# Q 207 : # where(sharing: true)
Query(Contact)
.where("sharing = ?")
# Q 208 : # where(type: "Reshare")
Query(Post)
.where("type = ?")
# Q 209 : # where(user_id: user.id)
Query(ShareVisibility)
.where("user_id = ?")
