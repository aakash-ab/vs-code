candidate_id
candidate_name

technology_id
category_id

class NameSerializer(serializers.ModelSerilizer):
    technology = TechnologySerializer(many=True)
    category = categorySerializer(many=True)

    def create(self, validated_data):
        technology = validated_data.pop('technology')
        category = validated_data.pop('category')
        naming = Name.objects.create(**validated_data)
        for techno in technology:
            Technology.objects.create(name=name_instance, **techno)
            return name_instance


num1 = (1,2,3,4)
num2 = (5,6,7,8)

new_num = num1 + num2
print(new_num)


new_list = [1,2,3]
print(convert(new_list))
new_list.append(new_num)
print(new_list)