from autogen.agentchat.contrib.agent_builder import AgentBuilder
import autogen
config_file_or_env = "OAI_CONFIG_LIST"
llm_config = {"temperature": 0}
config_list = autogen.config_list_from_json(config_file_or_env, filter_dict={"model": ["gpt-4-1106-preview", "gpt-4"]})


def start_task(execution_task: str, agent_list: list):
    group_chat = autogen.GroupChat(agents=agent_list, messages=[], max_round=12)
    manager = autogen.GroupChatManager(groupchat=group_chat, llm_config={"config_list": config_list, **llm_config})
    agent_list[0].initiate_chat(manager, message=execution_task)


builder = AgentBuilder(
    config_file_or_env=config_file_or_env, builder_model="gpt-4-1106-preview", agent_model="gpt-4-1106-preview"
)

building_task = "Generate some agents that can write a book about 3,000 words long.  Save each chapter in a directory as a txt file."


agent_list, agent_configs = builder.build(building_task, llm_config)


book = '''    Synopsis:

        "Eli's Awakening" narrates the transformative journey of Eli, once considered the black sheep of his family, subjected to relentless disparagement and devoid of love. Eli's life takes a pivotal turn when he discovers a profound connection with faith, opening his heart to the unconditional love and guidance of the divine.

        Through his spiritual journey, Eli undergoes a remarkable transformation, shedding the scars of his past to emerge as a symbol of hope, kindness, and resilience. His story illustrates the powerful message that it's never too late to change and find one's place of belonging and respect in the world. By the end, Eli is not only cherished and esteemed but also stands as a testament to the enduring strength of the human spirit and the redemptive power of faith.
        '''

saved_path = builder.save()


# start_task(
#     execution_task=book, agent_list=agent_list,
# )